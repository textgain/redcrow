from sklearn.externals import joblib
class arabicdialect():
    def __init__(self,classifier_type):
        if classifier_type == 'iraqi':
            self.pipe = joblib.load('iraqi.pkl')
        elif classifier_type == 'egyptian':
            self.pipe = joblib.load('egypt.pkl')
        elif classifier_type == 'multi':
            self.pipe = joblib.load('multi.pkl')
        else:
            raise ValueError("Classifier type is not available")
        
    def classify_one(self,document):
        return(self.pipe.predict([document])[0])
        
    def classify_many(self,documents):
        return(list(self.pipe.predict(documents)))