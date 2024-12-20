import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
def Seite2():
    st.write("This is your Data")
    data = np.random.randn(10, 5)
    st.write(data)
    # Plot data
    fig, ax = plt.subplots()
    ax.plot(data)
    st.pyplot(fig)
    