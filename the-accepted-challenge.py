#!/usr/bin/python3
"""
find all words that start with t and end with e here

The tree stands tall by the temple, its tangle of branches swaying in the gentle breeze. The twinkle of sunlight dances on each tide that kisses the terrace by the teal lake. A sense of tranquility fills the time, as birds traverse the sky with effortless tune. Beneath the table, a cat finds solace, its whiskers brushing against the smooth wooden texture. The scene captures a moment of pure treasure, untouched by the rush of modern trade.

"""
import re
paragraph = """The tree stands tall by the temple, its tangle of branches swaying in the gentle breeze. The twinkle of sunlight dances on each tide that kisses the terrace by the teal lake. A sense of tranquility fills the time, as birds traverse the sky with effortless tune. Beneath the table, a cat finds solace, its whiskers brushing against the smooth wooden texture. The scene captures a moment of pure treasure, untouched by the rush of modern trade."""
#print(paragraph)x = re.findall(r"\bT\w+s", paragraph, re.IGNORECASE)
x = re.findall(r"\bT\w+e", paragraph, re.IGNORECASE)
print(x)
