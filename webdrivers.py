from selenium import webdriver

def createDriver(**kwargs):
    
    navigator = kwargs.get('navigator', 'chrome')
    headless = kwargs.get('headless', False)
    width = kwargs.get('width', 800)
    height = kwargs.get('height', 600)

    print("Navegador corriendo en modo headless:", headless)

    
    def createChromiumWD():
        options = webdriver.ChromeOptions()
        options.add_argument('headless') if headless else None
        options.add_argument(f"--window-size={width},{height}")
        webDriver = webdriver.Chrome(options=options) 
        return webDriver
    

    def createFirefoxWD():
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless') if headless else None
        options.add_argument(f"--width={width}")  
        options.add_argument(f"--height={height}") 
        webDriver = webdriver.Firefox(options=options)
        return webDriver    
 
    options = {
        'chrome': createChromiumWD,
        'firefox': createFirefoxWD,
        
    }

    selected_function = options.get(navigator, lambda: None)
    return selected_function()