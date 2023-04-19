from loopgpt.agent import Agent

import argparse
import json


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("action", choices=["run"], help="Action to perform. If no file is specified, a new agent is created.")
    parser.add_argument("filename", nargs="?", help="Agent state JSON.", default=None)
    parser.add_argument(
        "--readonly",
        help="Read only mode. Does not write agent state to disk.",
        action="store_true",
    )
    parser.add_argument(
        "--reset",
        help="Reset agent state before use. Name, goals and description are not affected.",
        action="store_true",
    )
    parser.add_argument(
        "--save",
        help="Filename to save the agent. Only applicable when `filename` is not specified.",
    )

    args = parser.parse_args()

    filename = args.filename

    if filename is not None:
        with open(filename, "r") as f:
            agent_state = json.load(f)

        agent = Agent.from_config(agent_state)

        if args.reset:
            agent.clear_state()

        agent.cli()

        if not args.readonly:
            with open(filename, "w") as f:
                json.dump(agent.config(), f)
    else:
        agent = Agent()
        agent.cli()

        if args.save:
            with open(args.save, "w") as f:
                json.dump(agent.config(), f)
