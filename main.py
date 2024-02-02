import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header

def rain_baloons():
    rain(
        emoji="🎈",
        font_size=34,
        falling_speed=8,
        animation_length=4,
    )
def main():
    st.title("🚀Discover the Beauty of English")

    st.write(
        """
        English is a fascinating and versatile language that plays a crucial role in global communication.
        This website aims to showcase the importance and cool aspects of the English language.
        """
    )

    st.info("English is the #1 used language in the world!", icon="❗")

    # Section 1: Importance of English
    colored_header(
        label="📌Why is English Important?",
        description="",
        color_name="blue-70",
    )
#    st.header("Why is English Important?")
    st.write(
        """
        1. **Global Communication:** English is widely used as a global language, facilitating communication
           among people from different linguistic backgrounds.
        2. **Business Opportunities:** Proficiency in English enhances career prospects and opens up
           international business opportunities.
        3. **Cultural Exchange:** English is a key language for sharing ideas, literature, and culture on a global scale.
        """
    )

    # Section 2: Cool Aspects of English
    colored_header(
        label="😎Cool Aspects of English",
        description="",
        color_name="blue-70",
    )
#    st.header("Cool Aspects of English")
    st.write(
        """
        1. **Vast Vocabulary:** English has an extensive vocabulary, allowing for precise expression.
        2. **Literary Richness:** Enjoy a wealth of literature, from Shakespearean plays to modern novels.
        3. **Innovation in Language:** English continually evolves, embracing new words and expressions.
        """
    )

    # Section 3: Tips and Resources to Learn English
    colored_header(
        label="🎯Tips and Resources to Learn English",
        description="",
        color_name="blue-70",
    )
#    st.header("Tips and Resources to Learn English")
    st.write(
        """
        1. **Consistent Practice:** Regularly engage in reading, writing, speaking, and listening in English.
        2. **Online Courses:** Explore platforms like Duolingo, Babbel, or Coursera for structured language courses.
        3. **Language Exchange:** Connect with native English speakers for language exchange on platforms like Tandem.
        4. **Online quizes:** To improve your english skills you can use some online quizes to enhance your memorization skills.
        
        Our recomndation>> [Synonyms Quiz](https://votryfiras.github.io/Synonyms-quiz/)
        """
    )

if __name__ == "__main__":
    main()
