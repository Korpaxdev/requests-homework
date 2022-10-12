from stackoverflow import StackOverflow

if __name__ == "__main__":
    stackoverflow = StackOverflow()
    # Формат дат %d-%m-%Y
    questions = stackoverflow.get_questions('10-10-2022')
    print(questions)
