#statitics import for average and base list
import statistics as stats
study_data = []
#to add a data slot for a study session
def add_session():
  subject = input("Subject: ")
  minutes = int(input("Number of minutes studied: "))
  test_score = int(input("What score did you get on your test: "))

  session = {"subject": subject, "minutes": minutes, "test_score": test_score}

  study_data.append(session)
  print("Session added!")
# displays data in a simple format
def show_data():
  if not study_data:
    print("No sessions yet!")
    print()
    return
  for session in study_data:
    subject = session["subject"]
    minutes = session["minutes"]
    test_score = session["test_score"]
    print("Subject - " + subject + ", Minutes studied - " + str(minutes) + ", Test score - " + str(test_score))
    print()
# Recommends minutes based off of test score
def recommend_minutes():
  if not study_data:
    print("No sessions yet!")
  subject_scores = {}

  for session in study_data:
    subject = session["subject"]
    test_score = session["test_score"]

    # Make sure the key exists
    if subject not in subject_scores:
        subject_scores[subject] = []

    # Now append safely
    subject_scores[subject].append(test_score)
  
  for subject in subject_scores:
    avg = stats.mean(subject_scores[subject])
    if avg < 80:
      print("You should spend more time studying for " + subject + ".")
    else:
      print("You are doing good in " + subject + "!")
  print()
# menu

while True:
  print("1. Log a Study Session")
  print("2. Show Logged Study Session Data")
  print("3. Recommend Study Habit for Future")
  print("4. Quit")
  print()

  option = input("Choose an option: ")

  if option == "1":
    add_session()
  elif option == "2":
    show_data()
  elif option == "3":
    recommend_minutes()
  elif option == "4":
    break
  else:
    print("Invalid option, try again!")
