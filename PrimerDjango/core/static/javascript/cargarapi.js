        // Variables globales
let categorias = [];
let productosActuales = [];
let categoriaSeleccionada = null;
let noticias = [];
let noticiasGames= [];
let bannerDefault = null;


        // URLs de los endpoints
        const API_BASE = '/api';
        const ENDPOINTS = {
            categorias: `${API_BASE}/categorias/`,
            productos: `${API_BASE}/productos/`,
            productosPorCategoria: (id) => `${API_BASE}/productos/categoria/${id}/`,
            noticias: `${API_BASE}/noticias/gaming/`,
            noticiasGames: `${API_BASE}/noticias/games/`
        };

        // Función para mostrar/ocultar elementos
        function toggleElement(id, show) {
            const element = document.getElementById(id);
            if (element) {
                if (show) {
                    element.style.display = 'block';
                    element.classList.remove('d-none');
                } else {
                    element.style.display = 'none';
                    element.classList.add('d-none');
                }
            }
        }

        // Función para mostrar loading
        function mostrarLoading() {
            console.log('Mostrando loading...');
            toggleElement('loading', true);
            toggleElement('productsGrid', false);
            toggleElement('noProducts', false);
            document.getElementById('errorMessage').classList.add('d-none');
        }

        // Función para mostrar error
        function mostrarError(mensaje) {
            console.log('Mostrando error:', mensaje);
            toggleElement('loading', false);
            toggleElement('productsGrid', false);
            toggleElement('noProducts', false);
            const errorElement = document.getElementById('errorMessage');
            errorElement.classList.remove('d-none');
            document.getElementById('errorText').textContent = mensaje;
        }

        // Función para cargar categorías
        async function cargarCategorias() {
            try {
                const response = await fetch(ENDPOINTS.categorias);
                const data = await response.json();
                
                if (data.success) {
                    categorias = data.data;
                    renderizarCategorias();
                } else {
                    console.error('Error al cargar categorías:', data.message);
                }
            } catch (error) {
                console.error('Error de red al cargar categorías:', error);
            }
        }

        // Función para renderizar categorías en la navegación
        function renderizarCategorias() {
            const categoriesNav = document.getElementById('categoriesNav');
            const todosBtn = categoriesNav.querySelector('.all-products');
            
            // Limpiar categorías existentes (mantener botón "Todos")
            const categoriaBtns = categoriesNav.querySelectorAll('.category-btn:not(.all-products)');
            categoriaBtns.forEach(btn => btn.remove());
            
            // Agregar botones de categorías
            categorias.forEach(categoria => {
                const btn = document.createElement('button');
                btn.className = 'btn category-btn me-2 mb-2 mb-lg-0';
                btn.style='color: #b1b1b1;',
                btn.innerHTML = `<i class="fas fa-tag"></i> ${categoria.nombre}`;
                btn.onclick = () => mostrarProductosPorCategoria(categoria.id, categoria.nombre);
                categoriesNav.appendChild(btn);
            });
        }

        // Función para cargar todos los productos
        async function cargarTodosLosProductos() {
            console.log('Iniciando carga de productos...');
            mostrarLoading();
            
            try {
                console.log('Haciendo fetch a:', ENDPOINTS.productos);
                const response = await fetch(ENDPOINTS.productos);
                console.log('Respuesta recibida:', response.status);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log('Datos recibidos:', data);
                
                if (data.success) {
                    productosActuales = data.data;
                    console.log('Productos cargados:', productosActuales.length);
                    renderizarProductos();
                    document.getElementById('sectionTitle').innerHTML = 
                        '<i class="fas fa-shopping-bag"></i> Todos Nuestros Productos';
                } else {
                    console.error('Error en respuesta:', data.message);
                    mostrarError(data.message || 'Error al cargar productos');
                }
            } catch (error) {
                console.error('Error de red:', error);
                mostrarError('Error de conexión. Por favor, intenta nuevamente.');
            }
        }

        // Función para cargar productos por categoría
        async function cargarProductosPorCategoria(categoriaId, categoriaNombre) {
            mostrarLoading();
            
            try {
                const response = await fetch(ENDPOINTS.productosPorCategoria(categoriaId));
                const data = await response.json();
                
                if (data.success) {
                    productosActuales = data.data;
                    renderizarProductos();
                    document.getElementById('sectionTitle').innerHTML = 
                        `<i class="fas fa-tag"></i> ${categoriaNombre}`;
                } else {
                    mostrarError(data.message || 'Error al cargar productos de la categoría');
                }
            } catch (error) {
                console.error('Error de red:', error);
                mostrarError('Error de conexión. Por favor, intenta nuevamente.');
            }
        }

        // Función para renderizar productos
        function renderizarProductos() {
            console.log('Renderizando productos:', productosActuales.length);
            const productsGrid = document.getElementById('productsGrid');
            
            toggleElement('loading', false);
            
            if (productosActuales.length === 0) {
                console.log('No hay productos');
                toggleElement('noProducts', true);
                toggleElement('productsGrid', false);
                return;
            }
            
            console.log('Mostrando productos');
            toggleElement('noProducts', false);
            
            // Mostrar el grid usando Bootstrap classes
            productsGrid.style.display = 'flex';
            productsGrid.classList.remove('d-none');
            
            // Grid responsivo de Bootstrap: 
            // - sm: 1 columna en móviles pequeños
            // - md: 2 columnas en tablets 
            // - lg: 3 columnas en pantallas grandes
            // - xl: 4 columnas en pantallas extra grandes
            productsGrid.innerHTML = productosActuales.map(producto => `
                <div class="col-12 col-md-6 col-lg-4 col-xl-3">
                    <div class="card product-card text-bg-dark h-100">
                        <div class="product-image m-3">
                            <i class="fas fa-image"><img src="${producto.imagen}" class="card-img" alt="img_cat"></i>
                        </div>
                        <div class="card-body d-flex flex-column">
                            
                            <div class="mb-2">
                                <span class="badge product-category-badge">
                                    ${producto.categoria.nombre}
                                </span>
                            </div>
                            <h5 class="card-title product-name text-center">${producto.nombre}</h5>
                            <p class="card-text text-center text-white flex-grow-1">${producto.descripcion}</p>
                            <div class="text-center mt-auto">
                                <div class="product-price">$${parseFloat(producto.precio).toLocaleString('es-CL')}</div>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
        }

async function cargarNoticias() {
    try {
        const response = await fetch(ENDPOINTS.noticias);
        const data = await response.json();

        if (data.status === "ok" && data.articles) {
            renderizarNoticias(data.articles);
        } else {
            mostrarErrorNoticias(data.message || 'Error al cargar noticias');
        }
    } catch (error) {
        mostrarErrorNoticias('Error de conexión al cargar noticias');
    }
}

function renderizarNoticias(noticias) {
    const container = document.getElementById('noticiasContainer');
    if (!container) return;

    // Limitar a 3 noticias (puedes cambiar el número)
    const noticiasLimitadas = noticias.slice(0, 4);

    if (!noticiasLimitadas.length) {
        container.innerHTML = '<div class="col-12 text-center text-muted">No hay noticias disponibles.</div>';
        return;
    }

    container.style.display = 'flex';
    container.classList.remove('d-none');
    
    container.innerHTML = noticiasLimitadas.map(noticia => `
        <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4">
            <div class="card text-bg-dark h-100">
                <img src="${noticia.urlToImage}" class="card-img-top" alt="Imagen noticia">
                <div class="card-body">
                    <h5 class="card-title">${noticia.title}</h5>
                    <p class="card-text text-white">${noticia.description}</p>
                    <a href="${noticia.url}" target="_blank" class="btn btn-primary btn-sm">Ver más</a>
                </div>
            </div>
        </div>
    `).join('');
}

function mostrarErrorNoticias(mensaje) {
    const container = document.getElementById('noticiasContainer');
    if (container) {
        container.innerHTML = `<div class="col-12 text-center text-danger">${mensaje}</div>`;
    }
}

async function cargarNoticiasTwo() {
    try {
        const response = await fetch(ENDPOINTS.noticiasGames);
        const data = await response.json();

        if (Array.isArray(data)) {
            renderizarNoticiasTwo(data);
        } else {
            mostrarErrorNoticiasTwo(data.message || 'Error al cargar noticias');
        }
    } catch (error) {
        mostrarErrorNoticiasTwo('Error de conexión al cargar noticias');
    }
}

function renderizarNoticiasTwo(noticias) {
    const container = document.getElementById('noticiasContainerTwo');
    if (!container) return;

    // Limitar a 3 noticias (puedes cambiar el número)
    const noticiasLimitadas = noticias.slice(0, 4);

    if (!noticiasLimitadas.length) {
        container.innerHTML = '<div class="col-12 text-center text-muted">No hay noticias disponibles.</div>';
        return;
    }

    container.style.display = 'flex';
    container.classList.remove('d-none');
    
    container.innerHTML = noticiasLimitadas.map(noticia => `
        <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4">
            <div class="card text-bg-dark h-100">
                <img src="${noticia.main_image}" class="card-img-top" alt="Imagen noticia">
                <div class="card-body">
                    <h5 class="card-title">${noticia.title}</h5>
                    <p class="card-text text-white">${noticia.short_description}</p>
                    <a href="${noticia.article_url}" target="_blank" class="btn btn-primary btn-sm">Ver más</a>
                </div>
            </div>
        </div>
    `).join('');
}

function mostrarErrorNoticiasTwo(mensaje) {
    const container = document.getElementById('noticiasContainerTwo');
    if (container) {
        container.innerHTML = `<div class="col-12 text-center text-danger">${mensaje}</div>`;
    }
}

        // Función para mostrar todos los productos (desde botón)
        function mostrarTodosLosProductos() {
            categoriaSeleccionada = null;
            
            // Actualizar botones activos
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            document.querySelector('.category-btn.all-products').classList.add('active');

            document.getElementById('bannerCat').src = bannerDefault;
            
            cargarTodosLosProductos();
        }

        // Función para mostrar productos por categoría (desde botón)
        function mostrarProductosPorCategoria(categoriaId, categoriaNombre) {
            categoriaSeleccionada = categoriaId;
            
            // Actualizar botones activos
            document.querySelectorAll('.category-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');

            const categoria = categorias.find(cat => cat.id === categoriaId);
            if (categoria && categoria.imagen) {
            document.getElementById('bannerCat').src = categoria.imagen;
            }
            
            cargarProductosPorCategoria(categoriaId, categoriaNombre);
        }

        // Función de debug temporal
        function debugEndpoints() {
            console.log('=== DEBUG ENDPOINTS ===');
            console.log('API_BASE:', API_BASE);
            console.log('ENDPOINTS:', ENDPOINTS);
            console.log('URL actual:', window.location.href);
            console.log('Probando endpoints...');
            
            // Probar endpoint de productos
            fetch(ENDPOINTS.productos)
                .then(response => {
                    console.log('Respuesta productos:', response.status, response.statusText);
                    return response.json();
                })
                .then(data => {
                    console.log('Datos productos:', data);
                })
                .catch(error => {
                    console.error('Error productos:', error);
                });
        }

        // Inicializar la aplicación
        document.addEventListener('DOMContentLoaded', function() {
            // Marcar el botón "Todos" como activo inicialmente
            document.querySelector('.category-btn.all-products').classList.add('active');

            bannerDefault = document.getElementById('bannerCat').src;
            
            cargarCategorias();
            cargarTodosLosProductos();
            cargarNoticias();
            cargarNoticiasTwo();
        });