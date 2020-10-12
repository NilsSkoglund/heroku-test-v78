import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Hejsan")


st.write("test att deploya en uppdatering")


# Läs in csv-fil.
sthlm_df = pd.read_csv("sthlm_v1.csv")

# Lista som bara tar med gator som har minst 10 försäljningar
lista2 = sorted(sthlm_df.gata_lst.value_counts().loc[sthlm_df.gata_lst.value_counts() > 10].index.tolist())

# Widget där användare får ange vilken gata den vill se information om
option = st.selectbox(
    'Vilken gata vill du titta på?',
     lista2)

# Skapa df baserat på vald gata av användaren.
# Gör också om försäljningsdatum till datetime-format och sätter som index-kolumn
option_df = sthlm_df.loc[sthlm_df.gata_lst == option]
option_df.år_månad = pd.to_datetime(option_df.år_månad)
option_df.set_index("år_månad", inplace = True)

# output till användare
'Du valde: ', option
"Datan sträcker sig från:", str(option_df.index.min()).split()[0]
"Försäljningsdatum senast sålda lägenheten:", str(option_df.index.max()).split()[0]
st.write("Antalet sålda lägenheter under denna period:", len(option_df))

# Skapa lineplot med kr/kvm för varje objekt som sålts på gatan som användaren valt
sns.set(style = "whitegrid")
fig, ax = plt.subplots()
x = option_df.index
y = option_df.kr_kvm
ax.plot(x, y, c = "orange")
plt.ylabel("kr/kvm")
plt.ylabel("datum")
plt.title(f"Prisutv. {option}")
st.pyplot(fig)
