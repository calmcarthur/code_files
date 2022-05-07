const img_collage = document.getElementById('collage');
const img_arrow = document.getElementById('arrow');

const images = ["./mother/eating.jpg", "./mother/filter.jpg", "./mother/run.jpg", "./mother/smiling.jpg", "./mother/yum.jpg"];

function changePhoto() {
        
    let counter = -1;

    img_arrow.addEventListener('click', () => {
        counter += 1;

        if (counter === 5) {
            counter = 0;
        };

        img_collage.src = images[counter];

    });

};

changePhoto();