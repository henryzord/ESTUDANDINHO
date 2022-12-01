const html = document.querySelector("html")
const checkbox = document.querySelector("input[name=theme]")

const getStyle = (element, style) =>
    window
        .getComputedStyle(element)
        .getPropertyValue(style)

const initialColors = {
    bg: getStyle(html, "--bg"),
    bgFundo: getStyle(html, "--bg-fundo"),
    bgBagulhin: getStyle(html, "--bg-bagulhin"),
    bgLatera: getStyle(html, "--bg-latera"),
    bgHover: getStyle(html, "--bg-hover"),
    bgLetra: getStyle(html, "--bg-letra"),
}

const darkMode = {
    bg: "#15202b",
    bgFundo: "#3a4149",
    bgBagulhin: "#15202b",
    bgLatera: "#3a4149",
    bgHover: "#3c4c5c",
    bgLetra: "#ffffff",
}

const transformKey = key => "--" + key.replace(/([A-Z])/, "-$1").toLowerCase()

const changeColors = (colors) => {
    Object.keys(colors).map(key =>
        html.style.setProperty(transformKey(key), colors[key])
    )
}

checkbox.addEventListener("change", ({target}) => {
    target.checked ? changeColors(darkMode) : changeColors (initialColors)
})

