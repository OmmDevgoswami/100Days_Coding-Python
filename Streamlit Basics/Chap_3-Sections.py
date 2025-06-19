import streamlit as st

st.write("# Streamlit Sections Example")
st.write("## Welcome to your Grand Journey !! Please Choose Your Starter Pokemon.")
col1, col2, col3, col4 = st.columns(4, gap = "large")

with col1:
    st.write("## Charmendar")
    st.image("https://mystickermania.com/cdn/stickers/pokemon/pkm-charmander-512x512.png" , width = 100)
    choice1 = st.button("Charizard")

with col2:
    st.write("## Pikachu")
    st.image("https://i.pinimg.com/736x/29/54/6c/29546cc42fa517f38a56ba7db508ba56.jpg", width = 100)
    choice2 = st.button("Pikachu")
    
with col3:
    st.write("## Bulbasaur")
    st.image("https://preview.redd.it/4gxc5l2486x61.png?width=640&crop=smart&auto=webp&s=ebf33299cfa1434308a63fc133092a7a912a3bc8", width = 100)
    choice3 = st.button("Bulbasaur")

with col4:
    st.write("## Squirtle")
    st.image("https://miro.medium.com/v2/resize:fit:750/1*W_ITBT0_dDNGyy_yPRQO3g.jpeg", width = 100)
    choice4 = st.button("Squirtle")
    
if choice1:
    st.success(f"You Choosed Charmendar as your Partner-Pokemon !! Let Your Legendary Journey Unfold")
elif choice2:
    st.success(f"You Choosed Pikachu as your Partner-Pokemon !! Let Your Legendary Journey Unfold")
elif choice3:
    st.success(f"You Choosed Bulbasaur as your Partner-Pokemon !! Let Your Legendary Journey Unfold")
elif choice4:
    st.success(f"You Choosed Squirtle as your Partner-Pokemon !! Let Your Legendary Journey Unfold")

st.sidebar.write("## Trainer Card")
gender = st.sidebar.selectbox("Choose Your Gender:", ["Boy", "Girl"], index = None)
if gender == "Boy":
    st.sidebar.image("https://i.pinimg.com/736x/09/c9/9d/09c99d81cef75a2d25fa61137c7db833.jpg", width = 150)
elif gender == "Girl":
    st.sidebar.image("https://i.ebayimg.com/images/g/zm0AAOSw6wVlj5T7/s-l1200.png", width = 150)
    
trainer_name = st.sidebar.text_input("Enter your name: ")
st.sidebar.write(f"Welcome Trainer {trainer_name} into your Lagendary Journey")

with st.expander("## Your Badge Hunt: "):
    st.write("""1.Boulder Badge\n
2.Cascade Badge\n
3.Thunder Badge\n
4.Rainbow Badge\n
5.Soul Badge\n
6.Marsh Badge\n
7.Volcano Badge\n
8.Earth Badge""")
