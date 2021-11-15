mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
const PORT = process.env.PORT || 3000;\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
