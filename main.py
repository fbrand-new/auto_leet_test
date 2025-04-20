import argparse


def main():
    # This needs to be a cli with one argument: the number of the problem
    program_desc = "Autogenerates the unit test for the specified leetcode problem"
    parser = argparse.ArgumentParser(
        "auto_leet_test", "auto_leet_test problem_id", program_desc
    )

    parser.add_argument("problem_id", help="The problem id number", type=int)
    args = parser.parse_args()

    # Once we get the number of the problem from the user we can then fetch the corresponding webpage

    # Then we can extract the test case

    # Thereby creating a python file that runs the test. Maybe we should use templates.


if __name__ == "__main__":
    main()
