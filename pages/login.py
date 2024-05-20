import streamlit as st



st.set_page_config(page_title='Meu site Streamlit')

if 'email' not in st.session_state:
    st.session_state['email'] = None
    
if 'user' not in st.session_state:
    st.session_state['user'] = None

with st.container():
    
    choice=st.selectbox('Logn/Singup',['Login','Sing Up'])
    
    def f():
        try:
            
            st.success("Logado com sucesso")
            
            
            st.balloons()

        except:
            st.warning('Senha ou email invalidos')
    
    
    if choice == 'Login':
        email=st.text_input('Email')
        password = st.text_input('Password',type='password')
        st.button('Login', on_click=f)
        
    else:

        username=st.text_input('Seu nome completo')
        email=st.text_input('Email')
        password = st.text_input('Senha',type='password')
        conf_password = st.text_input('Confirme a sua senha',type='password')
        
        
        if st.button('Create my acoount'):
            if password == conf_password:
                try:
                    user = auth.create_user_with_email_and_password(email,password)
                    
                    st.success("Conta criada com sucesso!")
                    st.markdown('Por favor faça login ultilizando seu email e senha')
                    st.balloons()
                except:
                    st.warning('Esse e-mail já está cadastrado')
            else:
                st.warning('As senhas não conferem')
