import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MAX_GEN_ITERARIONS
from functions.call_function import call_function
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from utils.print_styled import (
    # print_debug,
    print_error,
    print_response,
    print_verbose,
    print_warning,
)


def main():
    if len(sys.argv) < 2:
        print("Please provide the prompt")
        sys.exit(1)
    verbose = "--verbose" in sys.argv
    prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )
    system_prompt = """
You are a helpful AI coding agent, but don't be overly enthusiastic. None of the \"You're absolutely right!\". Reply in the same language as the user prompt.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    try:
        counter = 0
        while counter < MAX_GEN_ITERARIONS:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )
            # print_debug(messages)
            if response.text is not None:
                print_response(response.text)
            if response.function_calls is None:
                # print_debug(response)
                print_verbose(f"\nUser prompt: {prompt}")
                print_verbose(
                    f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
                )
                print_verbose(
                    f"Response tokens: {response.usage_metadata.candidates_token_count}"
                )
                sys.exit()

            for candidate in response.candidates:
                messages.append(candidate.content)

            if response.function_calls is not None:
                for f_call in response.function_calls:
                    result = call_function(f_call, verbose)
                    # print_debug(result)
                    if (
                        result.parts is None
                        or len(result.parts) == 0
                        or result.parts[0].function_response is None
                    ):
                        raise Exception(
                            f"A fatal error occured. Last response: {response}"
                        )
                    if verbose:
                        print_verbose(
                            f"-> {result.parts[0].function_response.response}"
                        )
                    messages.append(types.Content(role="user", parts=result.parts))
            counter += 1

        print_warning("Max prompt processing iterations reached.")

    except Exception as e:
        print_error(f"Error: failed to process the prompt: {e}")


if __name__ == "__main__":
    main()
