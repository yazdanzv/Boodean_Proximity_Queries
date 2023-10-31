import os

# Create a directory to store the text files
if not os.path.exists(".\\Documents"):
    os.mkdir(".\\Documents")

# List of 40 sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "In the heart of the city, a bustling marketplace comes to life.",
    "Exploring distant galaxies, astronomers make groundbreaking discoveries.",
    "Ancient civilizations left behind mysteries waiting to be unraveled.",
    "Amidst the chaos, a lone musician plays a soulful melody on the streets.",
    "Sailing across the open ocean, a ship embarks on a grand adventure.",
    "In the depths of the forest, a hidden waterfall awaits the curious traveler.",
    "Scientists unveil a revolutionary technology that changes the world.",
    "Through the lens of a camera, moments are captured and memories preserved.",
    "A culinary masterpiece is crafted with love and creativity in the kitchen.",
    "The sound of laughter echoes through a sunlit park on a perfect day.",
    "Explorers venture into the unknown, seeking answers to age-old questions.",
    "An artist's canvas becomes a canvas for imagination and self-expression.",
    "Stories of courage and heroism inspire the next generation of leaders.",
    "Beneath the starry night sky, dreams take flight on the wings of hope.",
    "In the digital age, information flows freely, connecting people worldwide.",
    "A peaceful garden offers a sanctuary for quiet contemplation and reflection.",
    "As the sun sets, the horizon is painted with hues of orange and purple.",
    "Mystical creatures and legends come to life in the pages of a timeless book.",
    "In the heart of the city, diverse cultures converge, celebrating unity.",
    "The quick brown fox jumps over the lazy dog.",
    "In the heart of the city, a bustling marketplace comes to life with joy.",
    "Exploring distant galaxies, astronomers make groundbreaking discoveries about the universe.",
    "Ancient civilizations left behind mysteries waiting to be unraveled by archaeologists.",
    "Amidst the chaos, a lone musician plays a soulful melody on the streets of the vibrant city.",
    "Sailing across the open ocean, a ship embarks on a grand adventure to uncharted islands.",
    "In the depths of the forest, a hidden waterfall awaits the curious traveler seeking serenity.",
    "Scientists unveil a revolutionary technology that changes the world of medicine.",
    "Through the lens of a camera, moments are captured and memories preserved for generations.",
    "A culinary masterpiece is crafted with love and creativity in the kitchen of a renowned chef.",
    "The sound of laughter echoes through a sunlit park on a perfect summer day.",
    "Explorers venture into the unknown, seeking answers to age-old questions in uncharted territories.",
    "An artist's canvas becomes a canvas for imagination and self-expression through vivid colors.",
    "Stories of courage and heroism inspire the next generation of leaders worldwide.",
    "Beneath the starry night sky, dreams take flight on the wings of hope and aspiration.",
    "In the digital age, information flows freely, connecting people globally via the internet.",
    "A peaceful garden offers a sanctuary for quiet contemplation and reflection amid the urban hustle.",
    "As the sun sets, the horizon is painted with hues of orange and purple, creating a breathtaking view.",
    "Mystical creatures and legends come to life in the pages of a timeless fantasy book filled with enchantment.",
    "In the heart of the city, diverse cultures converge, celebrating unity and cultural exchange."
]

# Create and write sentences to 40 text files
for i, sentence in enumerate(sentences, start=1):
    if i < 10:
        index = f"0{i}"
    else:
        index = str(i)
    file_name = f".\\Documents\\doc{index}"
    with open(file_name, "w") as file:
        file.write(sentence)
