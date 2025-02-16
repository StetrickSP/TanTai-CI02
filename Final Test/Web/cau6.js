document.addEventListener('DOMContentLoaded', () => {
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(products => {
            const productContainer = document.createElement('div');
            productContainer.style.display = 'grid';
            productContainer.style.gridTemplateColumns = 'repeat(auto-fill, minmax(200px, 1fr))';
            productContainer.style.gap = '20px';
            document.body.appendChild(productContainer);

            products.forEach(product => {
                const productCard = document.createElement('div');
                productCard.style.border = '1px solid #ccc';
                productCard.style.padding = '10px';
                productCard.style.borderRadius = '5px';
                productCard.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';

                const productImage = document.createElement('img');
                productImage.src = product.image;
                productImage.alt = product.title;
                productImage.style.width = '100%';
                productImage.style.height = 'auto';

                const productTitle = document.createElement('h2');
                productTitle.textContent = product.title;
                productTitle.style.fontSize = '1.2em';
                productTitle.style.margin = '10px 0';

                const productPrice = document.createElement('p');
                productPrice.textContent = `$${product.price}`;
                productPrice.style.fontSize = '1em';
                productPrice.style.color = '#333';

                productCard.appendChild(productImage);
                productCard.appendChild(productTitle);
                productCard.appendChild(productPrice);
                productContainer.appendChild(productCard);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
});