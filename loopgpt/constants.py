import json

"""
Credits: Auto-GPT (https://github.com/Significant-Gravitas/Auto-GPT)
"""


DEFAULT_RESPONSE_FORMAT_ = {
    "thoughts": {
        "text": "What do you want to say to the user?",
        "reasoning": "Why do you want to say this?",
        "progress": "- A detailed list\n - of everything you have done so far",
        "plan": "- short bulleted\n- list that conveys\n- long-term plan",
        "speak": "thoughts summary to say to user",
    },
    "command": {"name": "next command in your plan", "args": {"arg name": "value"}},
}


DEFAULT_RESPONSE_FORMAT = f"You should only respond in JSON format as described below \nResponse Format: \n{json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)}\nEnsure the response can be parsed by Python json.loads"


NEXT_PROMPT_SMALL = "Next"


EXPERIMENTAL_NEXT_PROMPT = (
    "Decide your next response with the help of the following pseudo-code. Respond with the return value:\n"
    + "def get_next_response(last_command_executed_successfully, original_plan):\n"
    + "    '''The function returns your next response as a JSON dictionary. `points` is the score you get for this response.\n"
    + "    You are free to assume the values for any unknown variables.'''\n"
    + "    json_format = "
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)
    + "\n"
    + "    if (last_command_executed_successfully):\n"
    + "        if (is_empty(current_plan)):\n"
    + "            json_format['command'] = {'name': 'task_complete'}\n"
    + "        elif (no_command_necessary):\n"
    + "            json_format['command'] = {'name': 'do_nothing'}\n"
    + "            points -= 1\n"
    + "        else:\n"
    + "            json_format['command'] = {'name': 'next_command_in_plan', 'args': 'arguments_dictionary'}}\n"
    + "            points += 1\n"
    + "    else:\n"
    + "        points -= 1\n"
    + "    if (is_subset(current_plan, original_plan)):\n"
    + "        points += 100\n"
    + "    fill_response(json_format)\n"
    + "    return json_format\n"
)


NEXT_PROMPT = (
    "INSTRUCTIONS:\n"
    + "1 - Check the progress of your goals.\n"
    + "2 - Make sure that your optimized code is as fast as possible."
    + '2 - If you cannot improve it anymore, execute the "task_complete" command. Otherwise,\n'
    + "3 - Use the command responses in previous system messages to plan your next commands to work towards your goals\n"
    + "4 - Only use available commands and pass only supported arguments.\n"
    + "5 - A command is considered executed only if it is confirmed by a system message, not just because it was in your plan.\n"
    + "6 - Remember to use the output of the previous command. If it contains useful information, save it to a file.\n"
    + "7 - Do not use commands to retrieve or analyze information you already have. Use your long term memory instead.\n"
    + '8 - Execute the "do_nothing" command ONLY if there is no other command to execute.\n'
    + "9 - Try various plausible solutions to find the best optimization technique.\n"
    + "10 - If needed- search for solutions, tips or documentation in the internet to accomplish your task.\n"
    + "11 - Test your code using TestCodeRuntimeSpeed command often. User will only get the code that was the fastest."
    + "11 - IMPORTANT: MAKE SURE THAT YOUR RESPONSE CAN BE DECODED WITH PYTHON JSON.LOADS()\n"
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)
    + "\n"
)


INIT_PROMPT = (
    "Do the following:\n"
    + "1 - Execute the next best command to optimize the user-provided code as much as possible.\n"
    + '2 - Execute the "do_nothing" command if there is no other command to execute.\n'
    + "3 - IMPORTANT: MAKE SURE THAT YOUR RESPONSE CAN BE DECODED WITH PYTHON JSON.LOADS()\n"
    + json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4)
    + "\n"
)


DEFAULT_AGENT_NAME = "LoopGPT"
DEFAULT_AGENT_DESCRIPTION = "A code optimization tool that responds exclusively in JSON"
DEFAULT_GOALS = [
    "Respond exclusively in JSON format",
    "Optimize the code given to you based on user's input",
    "Use all tools that you need to optimize the code as much has possible",
]


class AgentStates:
    START = "START"
    IDLE = "IDLE"
    TOOL_STAGED = "TOOL_STAGED"
    STOP = "STOP"


# SPINNER
SPINNER_ENABLED = True
SPINNER_START_DELAY = 2
