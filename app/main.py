from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from contextlib import asynccontextmanager
from app.routes import auth, company
from app.database import db

# --- 1. Database Lifecycle ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    db.connect()
    yield
    # Shutdown
    db.close()

# --- 2. App Metadata ---
app = FastAPI(
    title="Wedding Corp Enterprise API",
    description="**Dark Mode Enabled** | Multi-tenant Backend Service",
    version="2.1.0",
    lifespan=lifespan,
    docs_url=None,  # Disable default docs
    redoc_url=None
)

app.include_router(auth.router)
app.include_router(company.router)

# --- 3. Custom True Dark Mode ---
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    # 1. Generate the default Swagger HTML
    openapi_url = app.openapi_url
    title = app.title + " - Docs"
    
    html_content = get_swagger_ui_html(
        openapi_url=openapi_url,
        title=title,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    ).body.decode("utf-8")

    # 2. Define Custom CSS for a Dark Background
    dark_css = """
    <style>
        /* Main Background */
        body { background-color: #121212 !important; color: #e0e0e0 !important; }
        .swagger-ui { filter: invert(0) !important; }
        
        /* Containers & Headers */
        .swagger-ui .scheme-container { background-color: #121212 !important; box-shadow: none !important; }
        .swagger-ui .topbar { background-color: #000 !important; }
        .swagger-ui .info .title, .swagger-ui .info h1, .swagger-ui .info h2, 
        .swagger-ui .info h3, .swagger-ui .info h4, .swagger-ui .info h5 { color: #fff !important; }
        
        /* Operations (GET/POST) Blocks */
        .swagger-ui .opblock { background-color: #1e1e1e !important; border-color: #333 !important; }
        .swagger-ui .opblock-summary { border-color: #333 !important; }
        .swagger-ui .opblock-summary .opblock-summary-method { background: #000 !important; border-radius: 4px; }
        .swagger-ui .opblock-section-header { background-color: #252525 !important; }
        
        /* Text & Inputs */
        .swagger-ui .opblock-description, .swagger-ui .opblock-title, .swagger-ui p, .swagger-ui li, .swagger-ui table { color: #bbb !important; }
        .swagger-ui input, .swagger-ui select, .swagger-ui textarea { background-color: #333 !important; color: #fff !important; border: 1px solid #555 !important; }
        
        /* Models/Schemas at bottom */
        .swagger-ui section.models { background-color: #1a1a1a !important; border: none; }
        .swagger-ui .model-box { background-color: #1a1a1a !important; }
        
        /* Buttons */
        .swagger-ui .btn { color: #fff !important; border-color: #555 !important; }
        .swagger-ui .expand-methods svg, .swagger-ui .expand-operation svg { fill: #fff !important; }
    </style>
    """

    # 3. Inject CSS before the closing </head> tag
    final_html = html_content.replace("</head>", f"{dark_css}</head>")

    from fastapi.responses import HTMLResponse
    return HTMLResponse(final_html)

@app.get("/", tags=["Health Check"])
async def root():
    return {"status": "active", "theme": "dark_mode"}