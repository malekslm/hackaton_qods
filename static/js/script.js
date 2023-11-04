const stringsToType = [
  "🇵🇸 نصر من الله و فتح قريب",
  "Victory from God and imminent triumph 🇵🇸",
  "神的胜利，即将的胜利 🇵🇸",
  "Victoria de Dios y triunfo inminente 🇵🇸",
  "Victoire de Dieu et triomphe imminent 🇵🇸",
  "Победа от Бога и неотвратимая победа 🇵🇸",
  "Sieg von Gott und bevorstehender Triumph 🇵🇸",
  "Vittoria da Dio e trionfo imminente 🇵🇸",
  "भगवान की विजय और आसन सफलता 🇵🇸",
  "Vitória de Deus e triunfo iminente 🇵🇸",
];

const textContainer = document.getElementById("text-container");
let stringIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeString() {
  const currentString = stringsToType[stringIndex];

  if (!isDeleting) {
    textContainer.innerHTML = currentString.substring(0, charIndex);
    charIndex++;

    if (charIndex > currentString.length) {
      isDeleting = true;
      setTimeout(typeString, 1000); // Pause before deleting
    } else {
      setTimeout(typeString, 50); // Typing speed
    }
  } else {
    textContainer.innerHTML = currentString.substring(0, charIndex);
    charIndex--;

    if (charIndex === 0) {
      isDeleting = false;
      stringIndex = (stringIndex + 1) % stringsToType.length;
      setTimeout(typeString, 500); // Pause before typing the next string
    } else {
      setTimeout(typeString, 50); // Deleting speed
    }
  }
}

typeString();


