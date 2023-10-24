#import pandas and read the dataset

import pandas as pd
data = pd.read_csv('\dataset.csv')

#filter rows with missing values
data = data.dropna(axis=0)

data.columns

#select features to work with
features = ['NumDots', 'SubdomainLevel', 'PathLevel', 'UrlLength', 'NumDash',
       'NumDashInHostname', 'AtSymbol', 'TildeSymbol', 'NumUnderscore',
       'NumPercent', 'NumQueryComponents', 'NumAmpersand', 'NumHash',
       'NumNumericChars', 'NoHttps', 'RandomString', 'IpAddress',
       'DomainInSubdomains', 'DomainInPaths', 'HttpsInHostname',
       'HostnameLength', 'PathLength', 'QueryLength', 'DoubleSlashInPath',
       'NumSensitiveWords', 'EmbeddedBrandName', 'PctExtHyperlinks',
       'PctExtResourceUrls', 'ExtFavicon', 'InsecureForms',
       'RelativeFormAction', 'ExtFormAction', 'AbnormalFormAction',
       'PctNullSelfRedirectHyperlinks', 'FrequentDomainNameMismatch',
       'FakeLinkInStatusBar', 'RightClickDisabled', 'PopUpWindow',
       'SubmitInfoToEmail', 'IframeOrFrame', 'MissingTitle',
       'ImagesOnlyInForm', 'SubdomainLevelRT', 'UrlLengthRT',
       'PctExtResourceUrlsRT', 'AbnormalExtFormActionR', 'ExtMetaScriptLinkRT',
       'PctExtNullSelfRedirectHyperlinksRT']

X = data[features]

#Choosing target label
y = data.CLASS_LABEL

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Taking all columns except URL
corr = data[features].corr()

fig = plt.figure(figsize=(12,12),dpi=80)
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, cmap='BuPu', robust=True, center=0,
            square=True, linewidths=.5)
plt.title('Correlation of Numerical(Continous) Features', fontsize=15,font="Serif")
plt.show()

df_distr = data.groupby('CLASS_LABEL')[features].mean().reset_index().T
df_distr.rename(columns={0: '0_Label', 1: '1_Label'}, inplace=True)

import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = 'w'
ax = df_distr[1:][['0_Label', '1_Label']].plot(kind='bar', title="Distribution of Average values across Target", figsize=(12, 8), legend=True, fontsize=12)
ax.set_xlabel("Numerical Features", fontsize=14)
ax.set_ylabel("Average Values", fontsize=14)
plt.show()

#importing required libraries
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#shuffling the data

from sklearn.utils import shuffle

X, y = shuffle(X, y, random_state=42)

#Scaling the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

#splitting the data into train and test sets
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.2, random_state=42)

import keras
import tensorflow as tf

model = keras.Sequential()

# Add input layer
model.add(keras.layers.Input(shape=(train_X.shape[1],)))

# Add hidden layers
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(32, activation='relu'))

# Add output layer
model.add(keras.layers.Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(train_X, train_y, epochs=10, batch_size=32, validation_data=(val_X, val_y))

test_loss, test_accuracy = model.evaluate(val_X, val_y)
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')

pred = model.predict(val_X)

val_y = val_y.astype(int)
pred = pred.astype(int)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


class_report = classification_report(val_y, pred, target_names=['Non-Phishing', 'Phishing'])
print("Classification Report:")
print(class_report)