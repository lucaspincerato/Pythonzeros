{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "agreed-rapid",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "homeless-fairy",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"VSS910.csv\", encoding  = \"UTF-8\", sep = \";\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "hundred-composition",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "incorporated-secretariat",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1048575 entries, 0 to 1048574\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   ReportDate                191 non-null    object \n",
      " 1   BusinessTransactionType   191 non-null    object \n",
      " 2   BusinessTransactionCycle  191 non-null    object \n",
      " 3   ReversalIndicator         191 non-null    object \n",
      " 4   Count                     191 non-null    float64\n",
      " 5   GrossAmount               191 non-null    object \n",
      " 6   InterchangeAmount         191 non-null    object \n",
      " 7   NetAmount                 191 non-null    object \n",
      " 8   DefermentDays             57 non-null     object \n",
      "dtypes: float64(1), object(8)\n",
      "memory usage: 72.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df.head()\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "plain-munich",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "smaller-indie",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"GrossAmount\"] = pd.to_numeric(df[\"GrossAmount\"], downcast=\"float\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "adult-retailer",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1048575 entries, 0 to 1048574\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   ReportDate                191 non-null    object \n",
      " 1   BusinessTransactionType   191 non-null    object \n",
      " 2   BusinessTransactionCycle  191 non-null    object \n",
      " 3   ReversalIndicator         191 non-null    object \n",
      " 4   Count                     191 non-null    float64\n",
      " 5   GrossAmount               191 non-null    float32\n",
      " 6   InterchangeAmount         191 non-null    object \n",
      " 7   NetAmount                 191 non-null    object \n",
      " 8   DefermentDays             57 non-null     object \n",
      "dtypes: float32(1), float64(1), object(7)\n",
      "memory usage: 68.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "empty-interval",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
