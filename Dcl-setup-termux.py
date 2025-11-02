#!/bin/bash

# =========================================================
# DCL SYSTEM SETUP - Premium Ultra
# By Doctor Coringa Lunático
# =========================================================

CONFIG_FILE="$HOME/.dcl_config"
TERMUX_COLORS="$HOME/.termux/colors.properties"

loading_bar() {
  local msg="$1"
  echo -ne "\n$msg "
  for i in {1..25}; do
    echo -ne "▓"
    sleep 0.05
  done
  echo -e " ✅"
  sleep 0.2
}

show_colors() {
  echo -e "\033[1;30m[0]\033[0m Preto"
  echo -e "\033[1;31m[1]\033[0m Vermelho"
  echo -e "\033[1;32m[2]\033[0m Verde"
  echo -e "\033[1;33m[3]\033[0m Amarelo"
  echo -e "\033[1;34m[4]\033[0m Azul"
  echo -e "\033[1;35m[5]\033[0m Magenta/Rosa"
  echo -e "\033[1;36m[6]\033[0m Ciano"
  echo -e "\033[1;37m[7]\033[0m Branco"
  echo -e "\033[1;90m[8]\033[0m Cinza Escuro"
  echo -e "\033[1;91m[9]\033[0m Vermelho Claro"
  echo -e "\033[1;92m[10]\033[0m Verde Claro"
  echo -e "\033[1;93m[11]\033[0m Amarelo Claro"
  echo -e "\033[1;94m[12]\033[0m Azul Claro"
  echo -e "\033[1;95m[13]\033[0m Rosa Claro"
  echo -e "\033[1;96m[14]\033[0m Ciano Claro"
  echo -e "\033[1;97m[15]\033[0m Branco Brilhante"
}

show_styles() {
  echo "[0] Normal"
  echo "[1] Negrito"
  echo "[2] Sublinhado"
  echo "[3] Itálico"
  echo "[4] Piscante"
  echo "[5] Invertido"
  echo "[6] 3D / Sombra"
}

get_color_code() {
  case $1 in
    0) echo "30" ;;
    1) echo "31" ;;
    2) echo "32" ;;
    3) echo "33" ;;
    4) echo "34" ;;
    5) echo "35" ;;
    6) echo "36" ;;
    7) echo "37" ;;
    8) echo "90" ;;
    9) echo "91" ;;
    10) echo "92" ;;
    11) echo "93" ;;
    12) echo "94" ;;
    13) echo "95" ;;
    14) echo "96" ;;
    15) echo "97" ;;
    *) echo "37" ;;
  esac
}

get_style_code() {
  case $1 in
    0) echo "0" ;;
    1) echo "1" ;;
    2) echo "4" ;;
    3) echo "3" ;;
    4) echo "5" ;;
    5) echo "7" ;;
    6) echo "8" ;;
    *) echo "0" ;;
  esac
}

# ==================== Tela Inicial ====================
clear
echo -e "\033[1;35m"
echo "╔════════════════════════════════════════╗"
echo "║        🌀 DCL SYSTEM INSTALLER 🌀      ║"
echo "╚════════════════════════════════════════╝"
echo -e "\033[0m"
sleep 0.8
echo -e "\033[1;36mBem-vindo ao DCL System Setup Premium Ultra!\033[0m"
sleep 0.8
echo "Aqui você vai criar seu próprio tema completo do Termux!"
sleep 0.8

# -------------------- Inputs do usuário --------------------
read -p "🖋️ Digite o texto do seu banner: " user_banner
echo ""
echo "🎨 Escolha a cor do texto principal:"
show_colors
read -p "Número da cor: " text_color_choice
echo ""
echo "🎨 Escolha a cor de fundo do texto:"
show_colors
read -p "Número da cor: " bg_color_choice
echo ""
echo "🖋️ Escolha o estilo do texto:"
show_styles
read -p "Número do estilo: " style_choice
echo ""
read -p "Digite o nome que quer ver no prompt: " user_prompt_name
echo ""
echo "🎨 Escolha a cor de fundo oficial do Termux (HEX, ex: #000000): "
read -p "Digite a cor: " termux_bg_color

# -------------------- Processando escolhas --------------------
text_color=$(get_color_code $text_color_choice)
bg_color=$(get_color_code $bg_color_choice)
style_code=$(get_style_code $style_choice)

# -------------------- Aplicando mudanças --------------------
echo -e "\n🔧 Aplicando seu tema..."
loading_bar "🎨 Configurando cores e fontes"
loading_bar "🖋️ Criando banner estilizado"
loading_bar "⚙️ Salvando preferências"
loading_bar "✨ Atualizando cor de fundo do Termux"

# Salva configurações
echo "$user_banner|$text_color|$bg_color|$style_code|$user_prompt_name" > "$CONFIG_FILE"

# Atualiza cor de fundo oficial do Termux
mkdir -p ~/.termux
echo "background=$termux_bg_color" > "$TERMUX_COLORS"
termux-reload-settings

# -------------------- Cria .bashrc customizado --------------------
cat > "$HOME/.bashrc" <<'EOF'
clear
CONFIG_FILE="$HOME/.dcl_config"
if [ -f "$CONFIG_FILE" ]; then
  IFS='|' read -r banner text_color bg_color style_code prompt_name < "$CONFIG_FILE"

  # Banner dentro de caixinha
  echo -e "\033[${style_code};${text_color};4${bg_color}m"
  echo "╔════════════════════════════════╗"
  printf "║ %-30s ║\n" "$banner"
  echo "╚════════════════════════════════╝"
  echo -e "\033[0m"

  # Prompt dentro de caixinha + símbolo
  PS1="╔═[$prompt_name]═╗ ➜ \w > "
fi
EOF

# -------------------- Alias global --------------------
echo "alias dclsetup='bash ~/dcl-setup-termux.sh'" >> ~/.bashrc

# Finalização
sleep 0.5
clear
echo -e "\033[1;32m✅ Instalação concluída com sucesso!\033[0m"
echo -e "\033[1;36m💙 Obrigado por usar DCL System Setup Premium Ultra!\033[0m"
echo -e "\033[1;36mFeche e abra o Termux e digite 'dclsetup' para rodar novamente seu setup!\033[0m"
