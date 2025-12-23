import datetime
import sys
import inflect
p = inflect.engine()

def main():
    try:
        year, month, day = input("Birth date: ").split("-")
    except ValueError:
        sys.exit("Invalid date")
    birth_date = datetime.date(int(year), int(month), int(day))
    today = datetime.date.today()
    substraction = today.__sub__(birth_date)
    minutes = substraction.days * 1440
    minutes_words = p.number_to_words(minutes)
    minutes_words = minutes_words.replace(" and ", " ")
    print(f"{minutes_words} minutes")



if __name__ == "__main__":
    main()