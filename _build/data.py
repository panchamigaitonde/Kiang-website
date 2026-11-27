"""Content for the Kiang site: films, trips, journal stories. Edit here, then run build.py."""

# ── Films ──
# credits: list of (person, role). kiang: Kiang Collective's role on the project, if any.
UPCOMING = [
    {"title": "Wild India", "by": "Terra Mater", "year": "2026", "status": "Completed · release to be announced",
     "credits": [], "kiang": "Line production and camera"},
    {"title": "Wild Day in Singapore", "by": "Terra Mater", "year": "2026", "status": "In post-production",
     "credits": [], "kiang": "Camera"},
    {"title": "Natural history film for NHK", "by": "NHK", "year": "", "status": "In post-production · title to be announced",
     "credits": [], "kiang": "Line production and camera"},
]

FEATURES = [
    {"title": "Raptors: A Fistful of Daggers", "by": "PBS Nature", "year": "2024", "yt": "_KyvkJb_AfE",
     "credits": [("Pradeep Hegde", "Camera")], "note": "Two-part series."},
    {"title": "Wild Tamil Nadu", "by": "Theatrical release", "year": "2026", "yt": "S7KbIu8pDag",
     "credits": [("Pradeep Hegde", "Camera")], "note": ""},
    {"title": "Project Tiger", "by": "Nature inFocus", "year": "2023", "yt": "Cweq9dMAMYE",
     "credits": [("Pradeep Hegde", "Camera")], "note": "Feature documentary marking 50 years of Project Tiger."},
    {"title": "Wild Karnataka", "by": "Discovery · Animal Planet", "year": "2019", "yt": "Ro9oZ8rQHxs",
     "credits": [("Pradeep Hegde", "Camera")], "note": ""},
    {"title": "Into the Wild India", "by": "", "year": "2018–2020", "yt": None, "poster": "poster-into-the-wild-india",
     "credits": [("Pradeep Hegde", "Camera")], "note": "Not currently available online."},
]

RG = "Roundglass Sustain"
DFE = "Directed, filmed and edited by Pradeep Hegde"
SHORTS = [
    {"title": "Batman and the Baavali: Bats of Bengaluru", "by": RG, "year": "2025", "yt": "sfhis5ORTpY", "credit": "Directed and filmed by Pradeep Hegde"},
    {"title": "The Land of Bears and Boulders: Daroji Sloth Bear Sanctuary", "by": RG, "year": "2025", "yt": "jbqn_ThRo20", "credit": DFE},
    {"title": "The Wilds of Daroji", "by": RG, "year": "2025", "yt": "HyRPGMd83eY", "credit": DFE},
    {"title": "Tibetan Sand Fox: The Highland Hunter", "by": RG, "year": "2023", "yt": "8o_H5424ySI", "credit": DFE},
    {"title": "The Grandala Blues", "by": RG, "year": "2023", "yt": "w3UD1iVAYlw", "credit": DFE},
    {"title": "Firefox of the Eastern Himalayas: Red Pandas", "by": RG, "year": "2023", "yt": "BDfjyPPmTNk", "credit": DFE},
    {"title": "The Misty Mountains of Singalila", "by": RG, "year": "2023", "yt": "6VryCcu4M80", "credit": DFE},
    {"title": "A Dust Spa: Malabar Pied Hornbills of Dandeli", "by": RG, "year": "2022", "yt": "FePtl5NrNBg", "credit": DFE},
    {"title": "Spiny Tailed Lizard's Day in the Sun", "by": RG, "year": "2020", "yt": "DA6Rivjt3N4", "credit": DFE},
    {"title": "Bishnois: Guardians of the Chinkara", "by": RG, "year": "2020", "yt": "niHvT0DT6d4", "credit": DFE},
    {"title": "Witness the Last Dance of the Great Indian Bustard", "by": RG, "year": "2020", "yt": "Lq-2IYafwZM", "credit": DFE},
    {"title": "Vultures: The Carrion Cleaners", "by": RG, "year": "2020", "yt": "Li5dI1Tn7iU", "credit": DFE},
    {"title": "The Thar Desert: The Secret Lives of a Harsh Desert", "by": RG, "year": "2020", "yt": "hqyaNrqZ8-c", "credit": DFE},
    {"title": "The Last Hop(e): Frogs of the Western Ghats", "by": "Independent", "year": "2019", "yt": "wzrTN59tr_I",
     "credit": "Directed, filmed, produced and edited by Pradeep Hegde"},
]

# ── Journal ──
STORIES = [
    {"slug": "journal-fireflies-in-valparai", "title": "Fireflies in Valparai", "place": "Valparai · Tamil Nadu",
     "image": "journal-fireflies-2", "alt": "A tree alive with fireflies in Valparai",
     "card": "journal-fireflies-2",
     "byline": "<b>Written by Panchami</b><br>Photograph by Sitara Karthikeyan",
     "related": ("journal.html", "More field notes", "Read the other stories from the field."),
     "body": [
        "When I've gone herping, I've always heard the phrase “the forest comes alive at night.” Most of the time that meant sounds to me — frogs, alarm calls, following the sounds of the forest. But this time, when the forest came alive, I saw it first.",
        "We'd step out of our rooms at 6 pm at the coffee estate in Valparai, just waiting for something magical. And I don't think I've seen anything like what happened next in my entire life.",
        "Tiny green light blobs would rise from the ground, from under the coffee plants. Within 30 to 45 minutes they'd reached the trees, and soon it looked exactly like standing under a Christmas tree, except the tree was alive and the lights were breathing.",
        "And then they'd start synchronising. A wave of light from one corner, slowly moving to the other, and back again. For hours.",
        "It goes completely beyond my understanding that something like this exists in the world. And that we get to witness it.",
     ]},
    {"slug": "journal-valley-of-flowers", "title": "Valley of Flowers", "place": "Valley of Flowers · Uttarakhand",
     "image": "journal-valley-portrait", "alt": "Pink wildflowers below a misty waterfall in the Valley of Flowers",
     "card": "journal-valley-portrait",
     "byline": "<b>Written by Panchami</b>",
     "related": ("expeditions.html", "Travel with us", "Small expeditions in the Himalaya, six guests at a time."),
     "body": [
        "As a kid, I saw places like this only in fairy tales and movies. Later I realised they actually exist, and I really wanted to see one.",
        "After I became a trek leader, I noticed everyone wanted to come here. It's one of those places people have heard about for years, so naturally, everyone shows up.",
        "But my friends and colleagues who led this trek told me what it's actually like on the ground. Flowers being plucked, people being careless, not really respecting how fragile the place is. Hearing all of this, I quietly hoped I'd never have to lead this trek.",
        "Recently, I got to spend a full week there during peak flowering season while filming. And I saw exactly what they'd described. The beauty, but also garbage, noise, and a general lack of care. It was honestly quite frustrating.",
        "Then it rained heavily for two days. There were landslide warnings and the trail shut from Govindghat, the base of the trek. No one could come up. We were stuck in Ghangaria, the first campsite.",
        "When the weather cleared, there were barely any people in the valley. And it felt completely different. No plucked flowers, no noise, no crowd. Just how it's supposed to be.",
        "I don't know if I was lucky, but I really wish more people got to see it like this. And more importantly, I hope people start showing up more responsibly.",
     ]},
    {"slug": "journal-most-beautiful-reptile", "title": "The Most Beautiful Reptile", "place": "Chalkewadi · Maharashtra",
     "image": "journal-lizard-2", "alt": "Fan-throated lizard on the laterite plateau at Chalkewadi",
     "card": "journal-lizard-2",
     "byline": "<b>Written by Panchami</b>",
     "related": ("films.html", "See the films", "Wildlife films our crew has worked on."),
     "body": [
        "I am someone who can never answer when someone asks me what my favourite animal is, or the most beautiful creature I've seen. But now, at least, I have an answer for one category. Most beautiful reptile. Fan throated lizard. At least until my next reptile shoot, I guess.",
        "We were at this laterite plateau in Maharashtra called Chalkewadi, which has the highest density of fan throated lizards. Almost every 100 metres, you see three or four of them. And their display is something else. So many colours — especially the blue, orange and black on their gular pouch, and this lovely yellowish tinge on their body.",
        "We spent about a week observing and filming one individual in his territory, and it was just beautiful to watch him go about his day.",
        "If you ever get a chance, do visit Chalkewadi. It's 30 km from Satara, and honestly the plateau itself is beautiful even without the lizards.",
     ]},
]
