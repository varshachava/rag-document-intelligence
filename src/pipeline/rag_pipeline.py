class RAGPipeline:

    def __init__(self, retriever, generator):

        self.retriever = retriever

        self.generator = generator

    def answer_question(self, question):

        documents = self.retriever.retrieve(question, 3)

        context = " ".join(documents)

        answer = self.generator.generate_answer(

            question,

            context

        )

        return answer
