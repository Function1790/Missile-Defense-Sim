const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

class Missile {

}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    requestAnimationFrame(render)
}

render()