{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "animated-munich",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "spatial-string",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"VSS910.csv\", encoding  = \"UTF-8\", sep = \";\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "conscious-french",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1048575 entries, 0 to 1048574\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count    Dtype         \n",
      "---  ------                    --------------    -----         \n",
      " 0   ReportDate                191 non-null      datetime64[ns]\n",
      " 1   BusinessTransactionType   1048575 non-null  object        \n",
      " 2   BusinessTransactionCycle  1048575 non-null  object        \n",
      " 3   ReversalIndicator         1048575 non-null  object        \n",
      " 4   Count                     191 non-null      float64       \n",
      " 5   GrossAmount               0 non-null        float64       \n",
      " 6   InterchangeAmount         0 non-null        float64       \n",
      " 7   NetAmount                 0 non-null        float64       \n",
      " 8   DefermentDays             0 non-null        float64       \n",
      "dtypes: datetime64[ns](1), float64(5), object(3)\n",
      "memory usage: 72.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "light-storage",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"GrossAmount\"] = pd.to_numeric(df[\"GrossAmount\"],errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "seven-tonight",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"InterchangeAmount\"] = pd.to_numeric(df[\"InterchangeAmount\"],errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "emotional-debate",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"NetAmount\"] = pd.to_numeric(df[\"NetAmount\"],errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "imperial-cattle",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"DefermentDays\"] = pd.to_numeric(df[\"DefermentDays\"],errors='coerce')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "departmental-smoke",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"ReportDate\"] = pd.to_datetime(df[\"ReportDate\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "fancy-bradley",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"BusinessTransactionType\"] = df[\"BusinessTransactionType\"].astype(\"str\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "minimal-earth",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"BusinessTransactionCycle\"] = df[\"BusinessTransactionCycle\"].astype(\"str\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "confident-andorra",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"ReversalIndicator\"] = df[\"ReversalIndicator\"].astype(\"str\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fancy-prisoner",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "stuck-moral",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "worthy-texture",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ReportDate</th>\n",
       "      <th>BusinessTransactionType</th>\n",
       "      <th>BusinessTransactionCycle</th>\n",
       "      <th>ReversalIndicator</th>\n",
       "      <th>Count</th>\n",
       "      <th>GrossAmount</th>\n",
       "      <th>InterchangeAmount</th>\n",
       "      <th>NetAmount</th>\n",
       "      <th>DefermentDays</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-01-01</td>\n",
       "      <td>Merchandise Credit</td>\n",
       "      <td>Originals</td>\n",
       "      <td>N</td>\n",
       "      <td>1037.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-01-01</td>\n",
       "      <td>Merchandise Credit</td>\n",
       "      <td>Originals</td>\n",
       "      <td>N</td>\n",
       "      <td>11743.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-01-01</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Dispute Financial</td>\n",
       "      <td>N</td>\n",
       "      <td>2571.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-01-01</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Dispute Response Financial</td>\n",
       "      <td>N</td>\n",
       "      <td>77.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-01-01</td>\n",
       "      <td>Purchase</td>\n",
       "      <td>Not Defined</td>\n",
       "      <td>Y</td>\n",
       "      <td>284.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ReportDate BusinessTransactionType    BusinessTransactionCycle  \\\n",
       "0 2021-01-01      Merchandise Credit                   Originals   \n",
       "1 2021-01-01      Merchandise Credit                   Originals   \n",
       "2 2021-01-01                Purchase           Dispute Financial   \n",
       "3 2021-01-01                Purchase  Dispute Response Financial   \n",
       "4 2021-01-01                Purchase                 Not Defined   \n",
       "\n",
       "  ReversalIndicator    Count  GrossAmount  InterchangeAmount  NetAmount  \\\n",
       "0                 N   1037.0          NaN                NaN        NaN   \n",
       "1                 N  11743.0          NaN                NaN        NaN   \n",
       "2                 N   2571.0          NaN                NaN        NaN   \n",
       "3                 N     77.0          NaN                NaN        NaN   \n",
       "4                 Y    284.0          NaN                NaN        NaN   \n",
       "\n",
       "   DefermentDays  \n",
       "0            NaN  \n",
       "1            NaN  \n",
       "2            NaN  \n",
       "3            NaN  \n",
       "4            NaN  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "verified-singer",
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
