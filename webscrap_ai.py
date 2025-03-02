import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

st.title('Web scrape AI agent')
st.caption('This app using openai and allow you to scrape a website using scrapegraph ai...')
openai_access_token = st.text_input('Open AI api Key', type= 'password')

if openai_access_token:
  model = st.radio(
      'select a model',
       ['gpt-3.5-turbo', 'gpt-4'],
      index=0,
  )
  graph_config = {
      "llm": {
          "api_key": openai_access_token,
          "model": model,
      },
  }
  url = st.text_input('Enter target URL...')
  user_prompt = st.text_input('What do you want to scrape? write your prompt here! ...')

  smart_scrape_graph = SmartScraperGraph(
      prompt = user_prompt,
      source = url,
      config=graph_config
  )


  if st.button('Scrape'):
    result = smart_scrape_graph.run()
    st.write(result)



