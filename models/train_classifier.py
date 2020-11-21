import sys
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
import pandas as pd
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import multioutput
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
import re
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import GridSearchCV
import pickle

def load_data(database_filepath):
    """
    Load data from database
    Input: data_filepath - String
           The file path / connection string to the database
           
           table_name - String
           The table that contains the data of interest
           
    Output: X - Pandas DataFrame
    """
    engine = create_engine('sqlite:///'+ str (database_filepath))
    df = pd.read_sql ('SELECT * FROM disaster', engine)
    X = df.loc[:, 'message']
    y = df.iloc[:, 4:]
    return X, y



def tokenize(text):
    """
    Tokenize 
    Input: Raw text
           
    Output: Lemmatized texts
    """
    #normalize text
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    # stopword list 
    stop_words = stopwords.words("english")
    #tokenize
    words = word_tokenize(text)
    #stemming
    stemmed = [PorterStemmer().stem(w) for w in words]
    #lemmatizing
    words_lemmed = [WordNetLemmatizer().lemmatize(w) for w in stemmed if w not in stop_words]
    return words_lemmed


def build_model():
    """
    Build the pipeline model that is going to be used as the model
    Input: word_dict - Dictionary
           The word dictionary from all of the messages
           
    Output: cv - model
            The model structure to be used for fitting and predicting
    """
    #setting pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', multioutput.MultiOutputClassifier (RandomForestClassifier()))
        ])


    #model parameters for GridSearchCV
   
    parameters = {'clf__estimator__max_depth': [1, 2, None]}
    cv = GridSearchCV (pipeline, param_grid= parameters, verbose =7 )
    return cv



def get_results(Y_test, y_pred):
    """
    Evaluation function, reports the f1 score, precision and recall for each output category of the dataset 
    Input: Y_test, y_pred
           
    Output: score, precision and recall
    """
    #Evaluation 
    results = pd.DataFrame(columns=['Category', 'f_score', 'precision', 'recall'])
    num = 0
    for cat in Y_test.columns:
        precision, recall, f_score, support = precision_recall_fscore_support(Y_test[cat], y_pred[:,num], average='weighted')
        results.set_value(num+1, 'Category', cat)
        results.set_value(num+1, 'f_score', f_score)
        results.set_value(num+1, 'precision', precision)
        results.set_value(num+1, 'recall', recall)
        num += 1
    print('Aggregated f_score:', results['f_score'].mean())
    print('Aggregated precision:', results['precision'].mean())
    print('Aggregated recall:', results['recall'].mean())
    return results

def evaluate_model(model, X_test, Y_test):
    """
    Evaluation function that calls get_results function to display the result
    """
    y_pred_tuned = model.predict(X_test)
    #converting to a dataframe
    #y_pred_tuned = pd.DataFrame(y_pred_tuned, columns = Y_test.columns)
    
    results_tuned = get_results(Y_test, y_pred_tuned)

    #display result of model evaluation
    print(results_tuned)



def save_model(model, model_filepath):
    """ Saving model's best_estimator_ using pickle
    """
    pickle.dump(model.best_estimator_, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        #X, Y, category_names = load_data(database_filepath)
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()