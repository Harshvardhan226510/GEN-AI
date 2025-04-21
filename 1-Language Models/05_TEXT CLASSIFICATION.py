from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts= ['I love AI.', 'I am goint to revolutionize AI.', 'AI is the future.', 'I love lions.', 'I love lions ego.', 'I love technology.', 'I love electric blue color.', 'I love super AI.', 'I love chatGPT.']

labels= ['AI', 'AI', 'AI', 'Lions', 'Lions', 'Technology', 'Color', 'AI', 'AI']

vectorizer= CountVectorizer()
x= vectorizer.fit_transform(texts)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
