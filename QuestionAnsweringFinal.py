def questionAnswering(context,question):
        from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
        model = QuestionAnsweringModel(
            "roberta", "outputs_QA/best_model", use_cuda=False)
        to_predict = [
            {
                "context": context,
                "qas": [
                    {
                        "question": question,
                        "id": "0",
                    }
                ],
            }
        ]
        answers, probabilities = model.predict(to_predict)
        #print(answers[0]['answer'][0])
        proba=probabilities[0]['probability'][0]*100
        #print(f'The probability percentage is {proba}')
        return answers[0]['answer'][0],proba