def recite(start_verse, end_verse):
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    verses = []
    for verse_num in range(start_verse, end_verse + 1):
        verse = f"On the {ordinals[verse_num - 1]} day of Christmas my true love gave to me: "
        for gift_num in range(verse_num, 0, -1):
            verse += gifts[gift_num - 1]
        verses.append(verse)

    return verses
