from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = ['i loved this movie', 'must watch movie', 'not worth watching', 'worst movie ever', 'brilliant movie']

labels = ['positive', 'positive', 'negative', 'negative', 'positive']

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

if accuracy > 0.8:
  print('movie is good book tickets!')
else:
  print('need to work on it')
