# @Author: hereiskunalverma
# @Date:   2022-05-02 09:16:34
# @Last Modified by:   hereiskunalverma
# @Last Modified time: 2022-05-02 09:16:59
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml