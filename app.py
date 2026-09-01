#!/usr/bin/env python3
"""
Senior Project Developer Profile

This script prints a short developer profile for the Senior Project.
"""

def get_profile():
	return {
		"Name": "Joshua Donatien",
		"Major": "Computer Science",
		"Technology Interest": (
			"Where AI can make a real difference: making tasks easier, more "
			"accessible, and cost-effective while improving efficiency"
		),
		"Skill Goal": (
			"Work end-to-end and develop job-ready backend skills"
		),
	}


def main():
	print("Senior Project Developer Profile\n")
	profile = get_profile()
	for key, value in profile.items():
		print(f"{key}: {value}")


if __name__ == "__main__":
	main()

