import sys as sys
from typing import Any
from flask import (Flask, Response, app, send_file, render_template,
                   request)
from duplex import calc_quad, calc_duplex, accumulated_materials, reset_variables, calc_decora, calc_gfci, calc_cutin, calc_surface, calc_duplex_controlled, calc_quad, calc_quad_decora, calc_quad_gfci, calc_quad_cutin, calc_quad_surface, calc_quad_controlled, calc_ff3, calc_ff4, calc_rough_data, calc_cutin_data, calc_lv_switch, calc_hv_switch, calc_hv_dimming, calc_wh_120, calc_wh_277, calc_ff3

# DEBUG = True
SITE_NAME = "Materialized"
FREEZER_BASE_URL = 'https:app.englishelectrical.net/'

app = Flask(__name__)

items = {}

@app.route('/count.html', methods=['GET', 'POST'])
def count():
    if request.method == 'POST':
        item = request.form['item']
        if item not in items:
            items[item] = 0
    return render_template('count.html', items=items)


@app.route('/calendar.html')
def calendar():
    # Pass the cell values to the template
    return render_template('calendar.html')


@app.route('/increment', methods=['POST'])
def increment():
    item = request.form['item']
    items[item] += 1
    return str(items[item])
  

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'], )  # type: ignore
def form() -> Any:
 
    
    
    # global decora, duplex_outlets, gfci, cutins, surface, quad_standard, duplex_controlled, four_square_box, four_square_bracket_box
    # If User hits the Generate button...
    # If Generate button is not pressed, just show index.html
    if request.method == 'POST':
        reset_variables()
        
        duplex_outlets = (request.form['standard'])
        if duplex_outlets:
            duplex_outlets = int(duplex_outlets)
        else:
            duplex_outlets  = 0  
                        
        decora = (request.form['decora'])
        if decora:
            decora = int(decora)
        else:
            decora  = 0  
            
        gfci = (request.form['gfci'])
        if gfci:
            gfci = int(gfci)
        else:
            gfci  = 0
            
        cutin = (request.form['cutin'])
        if cutin:
            cutin = int(cutin)
        else:
            cutin  = 0
            
        surface = (request.form['surface'])
        if surface:
            surface = int(surface)
        else:
            surface  = 0
            
        duplex_controlled = (request.form['1switch'])
        if duplex_controlled:
            duplex_controlled = int(duplex_controlled)
        else:
            duplex_controlled  = 0
        
        quad_standard = (request.form['quad_standard'])
        if quad_standard:
            quad_standard = int(quad_standard)
        else:
            quad_standard  = 0  
            
        quad_decora = (request.form['quad_decora'])
        if quad_decora:
            quad_decora = int(quad_decora)
        else:
            quad_decora  = 0
            
        quad_gfci = (request.form['quad_gfci'])
        if quad_gfci:
            quad_gfci = int(quad_gfci)
        else:
            quad_gfci  = 0
            
        quad_cutin = (request.form['quad_cutin'])
        if quad_cutin:
            quad_cutin = int(quad_cutin)
        else:
            quad_cutin  = 0
            
        quad_surface = (request.form['quad_surface'])
        if quad_surface:
            quad_surface = int(quad_surface)
        else:
            quad_surface  = 0
            
        quad_controlled = (request.form['quad_controlled'])
        if quad_controlled:
            quad_controlled = int(quad_controlled)
        else:
            quad_controlled  = 0

        ff3 = (request.form['3-wire'])
        if ff3:
            ff3 = int(ff3)
        else:
            ff3  = 0
            
        ff4 = (request.form['4-wire'])
        if ff4:
            ff4 = int(ff4)
        else:
            ff4  = 0

        rough_data = (request.form['rough_in_data'])
        if rough_data:
            rough_data = int(rough_data)
        else:
            rough_data  = 0
            
        cutin_data = (request.form['cutin_data'])
        if cutin_data:
            cutin_data = int(cutin_data)
        else:
            cutin_data  = 0


        lv_switch = (request.form['lv_switch'])
        if lv_switch:
            lv_switch = int(lv_switch)
        else:
            lv_switch  = 0
            
        hv_switch = (request.form['hv_switch'])
        if hv_switch:
            hv_switch = int(hv_switch)
        else:
            hv_switch  = 0
            
        hv_dimming = (request.form['hv_dimming'])
        if hv_dimming:
            hv_dimming = int(hv_dimming)
        else:
            hv_dimming  = 0

        wh_120 = (request.form['wh_120'])
        if wh_120:
            wh_120 = int(wh_120)
        else:
            wh_120  = 0
            
        wh_277 = (request.form['wh_277'])
        if wh_277:
            wh_277 = int(wh_277)
        else:
            wh_277  = 0
            
        calc_duplex(duplex_outlets) 
        calc_decora(decora)
        calc_gfci(gfci)
        calc_cutin(cutin)
        calc_surface(surface)
        calc_duplex_controlled(duplex_controlled)
    
        calc_quad(quad_standard)
        calc_quad_decora(quad_decora)
        calc_quad_gfci(quad_gfci)
        calc_quad_cutin(quad_cutin)
        calc_quad_surface(quad_surface)
        calc_quad_controlled(quad_controlled)
        
        calc_ff3(ff3)
        calc_ff4(ff4)
        calc_rough_data(rough_data)
        calc_cutin_data(cutin_data)
        calc_lv_switch(lv_switch)
        calc_hv_switch(hv_switch)
        calc_hv_dimming(hv_dimming)
        calc_wh_120(wh_120)
        calc_wh_277(wh_277) 
    
        return render_template('result.html', materials=accumulated_materials), reset_variables()
    
        #Redirect to result page
        # return redirect(url_for('result'))  # type: ignore
    # show html page
    return render_template('index.html')  # type: ignore

@app.route('/download') # type: ignore
def download() -> Response:
    filename = 'templates/new.xlsx'
    return send_file(filename, as_attachment=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    



@app.route('/todo.html')
def todo() -> str:   # show the form, it wasn't submitted
    return render_template('todo.html')


@app.route('/result.html')
def result():
    # Pass the cell values to the template
    return render_template('result.html')
    # return   send_file(filename, as_attachment=True, ) # type: ignore


@app.route('/manifest.json')  # type: ignore
def manifest() -> Response:
    return app.send_static_file('manifest.json')

# Serve service worker file


@app.route('/sw.js')
def service_worker() -> Response:
    return app.send_static_file('sw.js')

# Cache static assets


@app.after_request
def add_header(response) -> Response:
    response.headers['Cache-Control'] = 'static, max-age=31536000'
    return response


if __name__ == '__main__':
    app.run(debug = False, port = 8008, host = '0.0.0.0')
