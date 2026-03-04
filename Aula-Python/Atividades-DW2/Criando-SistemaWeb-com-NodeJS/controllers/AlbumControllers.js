import express from "express";
const router = express.Router();

export const albuns = [
  {
    title: "Master of Puppets",
    artist: "Metallica",
    ano: 1986,
    genero: "Metal",
    img: "/imgs/Master_of_Puppets.jpg"
  },
  {
    title: "Siamese Dream",
    artist: "The Smashing Pumpkins",
    ano: 1993,
    genero: "Rock Alternativo",
    img: "/imgs/Siamese_Dream.jpg"
  },
  {
    title: "Facelift",
    artist: "Alice in Chains",
    ano: 1990,
    genero: "Rock Alternativo",
    img: "/imgs/Facelift.jpg"
  },
  {
    title: "Ten",
    artist: "Pearl Jam",
    ano: 1991,
    genero: "Rock Alternativo",
    img: "/imgs/ten.jpg"
  },
  {
    title: "Weathered",
    artist: "Creed",
    ano: 2001,
    genero: "Rock Alternativo",
    img: "/imgs/Weathered.jpg"
  },
  {
    title: "Cowboys From Hell",
    artist: "Pantera",
    ano: 1990,
    genero: "Metal",
    img:  "/imgs/Cowboys_from_Hell.jpg"
  },
  {
    title: "Book of Shadows",
    artist: "Zakk Wylde",
    ano: 1996,
    genero: "Rock",
    img: "/imgs/book.jpg"
  },
  {
    title: "Siamês",
    artist: "Chococorn and the Sugarcanes",
    ano: 2023,
    genero: "Rock Alternativo",
    img: "/imgs/siames.jpg"
  },
  {
    title: "Repertorio Infindavel de Dolorosas Piadas",
    artist: "Gorduratrans",
    ano: 2015,
    genero: "Rock Alternativo",
    img: "/imgs/gorduratrans.jpg"
  },
  {
    title: "Alice in Chains - Unplugged",
    artist: "Alice in Chains",
    ano: 1996,
    genero: "Rock ALternativo",
    img:"/imgs/AIC_Unplugged.jpg"
  },
  {
    title: "Pronunced Leh-nerd Skin-nerd",
    artist: "Lynyrd Skynyrd",
    ano: 1972,
    genero: "Rock",
    img:"/imgs/Pronounced.jpg"
  },
  {
    title: "Snot",
    artist: "Snot",
    ano: 1997,
    genero: "Rock Alternativo",
    img:"/imgs/snot.jpg"
  },
  {
    title: "The Rise and Fall of a Midwest Princess",
    artist: "Chappell Roan",
    ano: 2023,
    genero: "Pop",
    img:"/imgs/Chappell.jpg"
  },
];

// Função para filtrar álbuns por gênero
export function getAlbunsPorGenero(genero) {
  return albuns.filter((album) => album.genero === genero);
}

// Rota padrão para listar todos os álbuns
router.get("/albuns", (req, res) => {
  res.render("albuns", { albuns });
});

export default router;
