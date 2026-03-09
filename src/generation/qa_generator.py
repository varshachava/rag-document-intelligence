from transformers import pipeline

class QAGenerator:

    def __init__(self, model_name):

        self.qa_pipeline = pipeline(

            "question-answering",

            model=model_name

        )

    def generate_answer(self, question, context):

        return self.qa_pipeline(

            question=question,

            context=context

        )
