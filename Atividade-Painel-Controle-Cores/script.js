//criando as variaveis para os botões
const container = document.getElementById("container");
const DarkButton = document.getElementById("DarkButton");
const LightButton = document.getElementById("LightButton");
const GrayButton = document.getElementById("GrayButton");

DarkButton.onclick = () => {
  container.style.backgroundColor = "#101010";
};

LightButton.onclick = () => {
  container.style.backgroundColor = "#fafafa";
};

GrayButton.onclick = () => {
  container.style.backgroundColor = "#1c1d22";
};
