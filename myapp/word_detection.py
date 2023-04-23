{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /Users/hanli/nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import nltk\n",
    "nltk.download('punkt')\n",
    "import string\n",
    "import pandas as pd\n",
    "ban_wds = pd.read_csv('swearWords.csv',header=None)\n",
    "ban_wds = ban_wds.values.tolist()[0]\n",
    "#Filter function\n",
    "def word_dect(text):\n",
    "    text_cln = text.lower()\n",
    "    text_cln = re.sub('[^A-Za-z0-9]+', ' ', text_cln) #word tokenization and preporcessing\n",
    "    text_cln = re.sub(r'[^\\w\\s]', '', text_cln)\n",
    "    tokens = nltk.word_tokenize(text_cln)\n",
    "    for i in tokens:\n",
    "        if i in ban_wds:\n",
    "            return 'Sensitive word detected!' \n",
    "            break\n",
    "        else:\n",
    "            continue\n",
    "    return text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ds",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
