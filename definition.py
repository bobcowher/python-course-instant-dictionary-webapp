import pandas
class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv("data.csv")
        return tuple(df.loc[df['word'] == self.term]['definition'])

#This section exists for testing purposes but won't run if it's called from a class. 
if __name__ == '__main__':
    definition = Definition(term="acid")
    print(definition.get())