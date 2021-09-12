#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "216ACD94-C70D-42CE-80F1-FA90A0D7F747",
  "name": "FutureOrPast",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631415223233,
  "passages": [
    {
      "name": "Present",
      "tags": "",
      "id": "1",
      "text": "Hello. I am your savior from the 5th-dimensional world. You are about to get sucked into the unknown loop of Blackhole due to a crack in time. If you want to escape from the infinite loop, find your way to get out of the loop or collect enough time crystals. \n\nFUTURE OR PAST\n\n[[FUTURE->Future]]\n[[PAST->Past]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Future",
          "original": "[[FUTURE->Future]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Past",
          "original": "[[PAST->Past]]"
        }
      ],
      "hooks": [],
      "cleanText": "Hello. I am your savior from the 5th-dimensional world. You are about to get sucked into the unknown loop of Blackhole due to a crack in time. If you want to escape from the infinite loop, find your way to get out of the loop or collect enough time crystals. \n\nFUTURE OR PAST"
    },
    {
      "name": "Future",
      "tags": "",
      "id": "2",
      "text": "Please pick LEFT OR RIGHT. (Type your pick)\n\n[[LEFT->Future no.48]]\n[[RIGHT->Future no.43]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Future no.48",
          "original": "[[LEFT->Future no.48]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Future no.43",
          "original": "[[RIGHT->Future no.43]]"
        }
      ],
      "hooks": [],
      "cleanText": "Please pick LEFT OR RIGHT. (Type your pick)"
    },
    {
      "name": "Past",
      "tags": "",
      "id": "3",
      "text": "Please pick LEFT or RIGHT. (Type your pick)\n\n[[LEFT->Past no.35]]\n[[RIGHT->Past no.32]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Past no.35",
          "original": "[[LEFT->Past no.35]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Past no.32",
          "original": "[[RIGHT->Past no.32]]"
        }
      ],
      "hooks": [],
      "cleanText": "Please pick LEFT or RIGHT. (Type your pick)"
    },
    {
      "name": "Future no.53",
      "tags": "",
      "id": "4",
      "text": "You are at age 53.\n\nConsistency is the key to escape from this catastrophe.\n\nFUTURE OR PAST\n\n[[PAST->Future no.48]]\n[[FUTURE->Future no.62]]",
      "links": [
        {
          "linkText": "PAST",
          "passageName": "Future no.48",
          "original": "[[PAST->Future no.48]]"
        },
        {
          "linkText": "FUTURE",
          "passageName": "Future no.62",
          "original": "[[FUTURE->Future no.62]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 53.\n\nConsistency is the key to escape from this catastrophe.\n\nFUTURE OR PAST"
    },
    {
      "name": "Future no.48",
      "tags": "",
      "id": "5",
      "text": "You are at age 48.\n\nDo not rush. It is just a beginning of your journey.\n\nFUTURE OR PAST\n\n[[FUTURE->Future no.53]] \n[[PAST->Present no.38]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Future no.53",
          "original": "[[FUTURE->Future no.53]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Present no.38",
          "original": "[[PAST->Present no.38]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 48.\n\nDo not rush. It is just a beginning of your journey.\n\nFUTURE OR PAST"
    },
    {
      "name": "Future no.75",
      "tags": "",
      "id": "6",
      "text": "Your age is 75. \n\nYou died at 73.",
      "links": [],
      "hooks": [],
      "cleanText": "Your age is 75. \n\nYou died at 73."
    },
    {
      "name": "Future no.43",
      "tags": "",
      "id": "7",
	  	"score": 1,
      "text": "You are at age 43.\n\nBeginner's luck? or not. Let's see how your time travel goes. \n\n1 Time Crystal.\n\nFUTURE OR PAST\n\n[[FUTURE->Future no.53]]\n[[PAST->Present no.38]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Future no.53",
          "original": "[[FUTURE->Future no.53]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Present no.38",
          "original": "[[PAST->Present no.38]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 43.\n\nBeginner's luck? or not. Let's see how your time travel goes. \n\n1 Time Crystal.\n\nFUTURE OR PAST"
    },
    {
      "name": "Past no.35",
      "tags": "",
      "id": "8",
	  	"score": 1,
      "text": "You are at age 35.\n\nBeginner's luck? or not. Let's see how your time travel goes. \n\n1 Time Crystal.\n\nFUTURE OR PAST\n\n[[PAST->Past no.28]]\n[[FUTURE->Present no.38]]",
      "links": [
        {
          "linkText": "PAST",
          "passageName": "Past no.28",
          "original": "[[PAST->Past no.28]]"
        },
        {
          "linkText": "FUTURE",
          "passageName": "Present no.38",
          "original": "[[FUTURE->Present no.38]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 35.\n\nBeginner's luck? or not. Let's see how your time travel goes. \n\n1 Time Crystal.\n\nFUTURE OR PAST"
    },
    {
      "name": "Past no.32",
      "tags": "",
      "id": "9",
      "text": "You are at age 32.\n\nDo not rush. It is just a beginning of your journey.\n\nFUTURE OR PAST\n\n[[FUTURE->Present no.38]]\n[[PAST->Past no.28]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Present no.38",
          "original": "[[FUTURE->Present no.38]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Past no.28",
          "original": "[[PAST->Past no.28]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 32.\n\nDo not rush. It is just a beginning of your journey.\n\nFUTURE OR PAST"
    },
    {
      "name": "Whole New World",
      "tags": "",
      "id": "10",
      "text": "You finally went out from the infinite time loop. \n\nYou are Welcome.",
      "links": [],
      "hooks": [],
      "cleanText": "You finally went out from the infinite time loop. \n\nYou are Welcome."
    },
    {
      "name": "Present no.38",
      "tags": "",
      "id": "11",
      "text": "You are back at your age.\n\nDo not waste your time. Time is ticking.\n\nFUTURE OR PAST OR UNKNOWN\n\n[[UNKNOWN->Somewhere in the middle of a time crack]]\n[[FUTURE->Future no.53]]\n[[PAST->Past no.28]]",
      "links": [
        {
          "linkText": "UNKNOWN",
          "passageName": "Somewhere in the middle of a time crack",
          "original": "[[UNKNOWN->Somewhere in the middle of a time crack]]"
        },
        {
          "linkText": "FUTURE",
          "passageName": "Future no.53",
          "original": "[[FUTURE->Future no.53]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Past no.28",
          "original": "[[PAST->Past no.28]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are back at your age.\n\nDo not waste your time. Time is ticking.\n\nFUTURE OR PAST OR UNKNOWN"
    },
    {
      "name": "Past no.28",
      "tags": "",
      "id": "12",
      "text": "You are at age 28.\n\nConsistency is the key to escape from this catastrophe.\n\nFUTURE OR PAST\n\n[[PAST->Past no.12]]\n[[FUTURE->Past no.32]]",
      "links": [
        {
          "linkText": "PAST",
          "passageName": "Past no.12",
          "original": "[[PAST->Past no.12]]"
        },
        {
          "linkText": "FUTURE",
          "passageName": "Past no.32",
          "original": "[[FUTURE->Past no.32]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 28.\n\nConsistency is the key to escape from this catastrophe.\n\nFUTURE OR PAST"
    },
    {
      "name": "Future no.47",
      "tags": "",
      "id": "13",
	  	"score": 2,
      "text": "You are at age 47.\n\nSometimes it is good to take the long way round. See?\n\n2 Time Crystals.\n\nFUTURE OR PAST\n\n[[FUTURE->Future no.65]]\n[[PAST->Future no.53]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Future no.65",
          "original": "[[FUTURE->Future no.65]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Future no.53",
          "original": "[[PAST->Future no.53]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 47.\n\nSometimes it is good to take the long way round. See?\n\n2 Time Crystals.\n\nFUTURE OR PAST"
    },
    {
      "name": "Future no.65",
      "tags": "",
      "id": "14",
      "text": "You are at age 65.\n\nI suppose you are almost there, but I am not 100% sure.\n\nFUTURE OR PAST\n\n[[FUTURE->Whole New World]]\n[[PAST->Future no.53]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Whole New World",
          "original": "[[FUTURE->Whole New World]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Future no.53",
          "original": "[[PAST->Future no.53]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 65.\n\nI suppose you are almost there, but I am not 100% sure.\n\nFUTURE OR PAST"
    },
    {
      "name": "Past no.12",
      "tags": "",
      "id": "15",
	  	"score": 1,
      "text": "You are at age 12.\n\nI recommend to keep going backwards... but it's your life, your choice.\n\n1 Time Crystal.\n\nFUTURE OR PAST\n\n[[FUTURE->Past no.21]]\n[[PAST->Past no.16]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Past no.21",
          "original": "[[FUTURE->Past no.21]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Past no.16",
          "original": "[[PAST->Past no.16]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 12.\n\nI recommend to keep going backwards... but it's your life, your choice.\n\n1 Time Crystal.\n\nFUTURE OR PAST"
    },
    {
      "name": "Past no.21",
      "tags": "",
      "id": "16",
	  	"score": 2,
      "text": "You are at age 21.\n\nSometimes it is good to take the long way round. See?\n\n2 Time Crystals.\n\nFUTURE OR PAST\n\n[[FUTURE->Past no.28]]\n[[PAST->Past no.16]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Past no.28",
          "original": "[[FUTURE->Past no.28]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Past no.16",
          "original": "[[PAST->Past no.16]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 21.\n\nSometimes it is good to take the long way round. See?\n\n2 Time Crystals.\n\nFUTURE OR PAST"
    },
    {
      "name": "Past no.16",
      "tags": "",
      "id": "17",
      "text": "You are at age 16.\n\nI suppose you are almost there, but I am not 100% sure.\n\nFUTURE OR PAST\n\n[[PAST->Whole New World]]\n[[FUTURE->Past no.28]]",
      "links": [
        {
          "linkText": "PAST",
          "passageName": "Whole New World",
          "original": "[[PAST->Whole New World]]"
        },
        {
          "linkText": "FUTURE",
          "passageName": "Past no.28",
          "original": "[[FUTURE->Past no.28]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 16.\n\nI suppose you are almost there, but I am not 100% sure.\n\nFUTURE OR PAST"
    },
    {
      "name": "Somewhere in the middle of a time crack",
      "tags": "",
      "id": "18",
	  	"score": 3,
      "text": "Your age is unknown.\n\nSometimes You Need To Turn Back.\n\n3 Time Crystals.\n\nFORWARD OR BACKWARD\n\n[[FORWARD->Future no.75]]\n[[BACKWARD->Present no.38]]",
      "links": [
        {
          "linkText": "FORWARD",
          "passageName": "Future no.75",
          "original": "[[FORWARD->Future no.75]]"
        },
        {
          "linkText": "BACKWARD",
          "passageName": "Present no.38",
          "original": "[[BACKWARD->Present no.38]]"
        }
      ],
      "hooks": [],
      "cleanText": "Your age is unknown.\n\nSometimes You Need To Turn Back.\n\n3 Time Crystals.\n\nFORWARD OR BACKWARD"
    },
    {
      "name": "Future no.62",
      "tags": "",
      "id": "19",
	  	"score": 1,
      "text": "You are at age 62.\n\nI recommend to keep going forwards... but it's your life, your choice.\n\n1 Time Crystal.\n\nFUTURE OR PAST\n\n[[FUTURE->Future no.65]]\n[[PAST->Future no.47]]",
      "links": [
        {
          "linkText": "FUTURE",
          "passageName": "Future no.65",
          "original": "[[FUTURE->Future no.65]]"
        },
        {
          "linkText": "PAST",
          "passageName": "Future no.47",
          "original": "[[PAST->Future no.47]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at age 62.\n\nI recommend to keep going forwards... but it's your life, your choice.\n\n1 Time Crystal.\n\nFUTURE OR PAST"
    }
  ]
}

# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: {}, Score: {}".format(moves, score))
		print("You are in the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("Your Move?\n")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label

# ----------------------------------------------------------------

from random import randint
location_label = "Present"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	if moves >= randint(8,12):
		print("You have wasted too much time. You have failed to escape from the loop.")
		break
	render(current_location, score, moves)
	if current_location["name"] == "Whole New World" or current_location["name"] == "Future no.75":
		break
	if score >= randint(5,8):
		print("You have successfully collected all your time crystals. Feel free to escape from the time loop.")
		break
	response = get_input()

print("THE END")