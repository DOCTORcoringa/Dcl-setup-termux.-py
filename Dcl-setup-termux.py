#!/bin/bash

CONFIG_FILE="$HOME/.dcl_config"

# Função para animação de carregamento
loading_bar() {
  local msg=$1
  echo -ne "\n$msg "
  for i in {1..20}; do
    echo -ne "▓"
    sleep 0.08
  done
  echo -e "  ✅"
  sleep 0.5
}

# Função para mostrar cores
show_colors() {
  echo -e "\033[1;31m[1]\033[0m Vermelho"
  echo -e "\033[1;32m[2]\033[0m Verde"
  echo -e "\033[1;33m[3]\033[0m Amarelo"
  echo -e "\033[1;34m[4]\033[0m Azul"
  echo -e "\033[1;35m[5]\033[0m Roxo"
  echo -e "\033[1;36m[6]\033[0m Ciano"
  echo -e "\033[1;37m[7]\033[0m Branco"
}

# Função para mostrar estilos de fonte
show_fonts() {
  echo "[1] Normal"
  echo "[2] Negrito"
  echo "[3] Itálico"
  echo "[4] Sublinhado"
}

# Tela inicial
clear
echo -e "\033[1;35m"
echo "╔════════════════════════════════════════════════════╗"
echo "║             🌀 DCL SYSTEM INSTALLER 🌀              ║"
echo "║               by Doctor Coringa Lunático           ║"
echo "╚════════════════════════════════════════════════════╝"
echo -e "\033[0m"
sleep 1

echo -e "\033[1;36mBem-vindo ao sistema de personalização DCL System!"
sleep 1
echo "Aqui você poderá criar seu próprio tema visual do Termux!"
sleep 2
echo -e "\033[0m"

# Inputs
read -p "🖋️ Digite o texto do seu banner: " user_banner
echo ""
echo "🎨 Escolha a cor do texto principal:"
show_colors
read -p "Número da cor: " text_color_choice
echo ""
echo "🎨 Escolha a cor de fundo:"
show_colors
read -p "Número da cor: " bg_color_choice
echo ""
echo "🖋️ Escolha o tipo de fonte:"
show_fonts
read -p "Número da fonte: " font_choice

# Traduz cores
get_color_code() {
  case $1 in
    1) echo "31" ;;
    2) echo "32" ;;
    3) echo "33" ;;
    4) echo "34" ;;
    5) echo "35" ;;
    6) echo "36" ;;
    7) echo "37" ;;
    *) echo "37" ;;
  esac
}

text_color=$(get_color_code $text_color_choice)
bg_color=$(get_color_code $bg_color_choice)
style_code="0"
case $font_choice in
  1) style_code="0" ;;
  2) style_code="1" ;;
  3) style_code="3" ;;
  4) style_code="4" ;;
esac

clear
echo -e "\033[1;35m🔧 Aplicando seu tema personalizado...\033[0m"
sleep 0.8
loading_bar "🎨 Configurando cores"
loading_bar "🖋️ Aplicando fontes"
loading_bar "⚙️ Salvando preferências"
loading_bar "✨ Finalizando instalação"

# Salva configurações
echo "$user_banner|$text_color|$bg_color|$style_code" > "$CONFIG_FILE"

# Cria o bashrc
cat > "$HOME/.bashrc" <<'EOF'
clear
config_file="$HOME/.dcl_config"
if [ -f "$config_file" ]; then
  IFS='|' read -r user_banner text_color bg_color style_code < "$config_file"
  echo -e "\033[${style_code};${text_color};4${bg_color}m"
  echo "╔════════════════════════════════════════════════════╗"
  echo "║                🌀 DCL SYSTEM 🌀                     ║"
  echo "║          by Doctor Coringa Lunático                ║"
  echo "╚════════════════════════════════════════════════════╝"
  echo ""
  echo -e "💫 $user_banner"
  echo -e "\033[0m"
else
  echo "DCL System - configuração não encontrada."
fi
EOF

sleep 0.5
clear
echo -e "\033[1;32m✅ Instalação concluída com sucesso!\033[0m"
sleep 0.5
echo ""
echo -e "\033[1;36mAgradecemos por usar o DCL System 💙"
echo "Criado por Doctor Coringa Lunático 🌀"
echo -e "Feche e reabra o Termux para ver o novo visual!\033[0m"
