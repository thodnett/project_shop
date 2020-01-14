{"filter":false,"title":"views.py","tooltip":"/cart/views.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":4,"column":0},"end":{"row":34,"column":41},"action":"insert","lines":["def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"],"id":3}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","],"id":4}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":5},{"start":{"row":0,"column":37},"end":{"row":0,"column":38},"action":"insert","lines":["r"]},{"start":{"row":0,"column":38},"end":{"row":0,"column":39},"action":"insert","lines":["e"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["v"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["e"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["s"],"id":6},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"remove","lines":["e"],"id":7},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"remove","lines":["s"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"remove","lines":["r"]},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"remove","lines":["e"]},{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"remove","lines":["v"]}],[{"start":{"row":0,"column":39},"end":{"row":0,"column":40},"action":"insert","lines":["d"],"id":8},{"start":{"row":0,"column":40},"end":{"row":0,"column":41},"action":"insert","lines":["i"]},{"start":{"row":0,"column":41},"end":{"row":0,"column":42},"action":"insert","lines":["r"]},{"start":{"row":0,"column":42},"end":{"row":0,"column":43},"action":"insert","lines":["e"]},{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":["c"]},{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"remove","lines":["r"],"id":9}],[{"start":{"row":0,"column":44},"end":{"row":0,"column":45},"action":"insert","lines":["t"],"id":10}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":[" "],"id":11}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"remove","lines":[" "],"id":12}],[{"start":{"row":0,"column":45},"end":{"row":0,"column":46},"action":"insert","lines":[","],"id":13}],[{"start":{"row":0,"column":46},"end":{"row":0,"column":47},"action":"insert","lines":[" "],"id":14},{"start":{"row":0,"column":47},"end":{"row":0,"column":48},"action":"insert","lines":["r"]},{"start":{"row":0,"column":48},"end":{"row":0,"column":49},"action":"insert","lines":["e"]},{"start":{"row":0,"column":49},"end":{"row":0,"column":50},"action":"insert","lines":["v"]},{"start":{"row":0,"column":50},"end":{"row":0,"column":51},"action":"insert","lines":["e"]},{"start":{"row":0,"column":51},"end":{"row":0,"column":52},"action":"insert","lines":["r"]},{"start":{"row":0,"column":52},"end":{"row":0,"column":53},"action":"insert","lines":["s"]},{"start":{"row":0,"column":53},"end":{"row":0,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":54},"end":{"row":0,"column":55},"action":"insert","lines":[" "],"id":15}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":34,"column":41},"end":{"row":34,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1575308970300,"hash":"11ac481e1e1411d5001ec3487044b1659bfbf8eb"}