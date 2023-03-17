function s(e, t) {
    for (var n = (e = e || "").length % 16, r = e.length - n, o = [0, t = t || 0], i = [0, t], a = [0, 0], s = [0, 0], u = [2277735313, 289559509], c = [1291169091, 658871167], l = 0; l < r; l += 16)
        a = [255 & e.charCodeAt(l + 4) | (255 & e.charCodeAt(l + 5)) << 8 | (255 & e.charCodeAt(l + 6)) << 16 | (255 & e.charCodeAt(l + 7)) << 24, 255 & e.charCodeAt(l) | (255 & e.charCodeAt(l + 1)) << 8 | (255 & e.charCodeAt(l + 2)) << 16 | (255 & e.charCodeAt(l + 3)) << 24],
        s = [255 & e.charCodeAt(l + 12) | (255 & e.charCodeAt(l + 13)) << 8 | (255 & e.charCodeAt(l + 14)) << 16 | (255 & e.charCodeAt(l + 15)) << 24, 255 & e.charCodeAt(l + 8) | (255 & e.charCodeAt(l + 9)) << 8 | (255 & e.charCodeAt(l + 10)) << 16 | (255 & e.charCodeAt(l + 11)) << 24],
        a = g(a, u),
        a = d(a, 31),
        a = g(a, c),
        o = m(o, a),
        o = d(o, 27),
        o = f(o, i),
        o = f(g(o, [0, 5]), [0, 1390208809]),
        s = g(s, c),
        s = d(s, 33),
        s = g(s, u),
        i = m(i, s),
        i = d(i, 31),
        i = f(i, o),
        i = f(g(i, [0, 5]), [0, 944331445]);
    switch (a = [0, 0],
    s = [0, 0],
    n) {
    case 15:
        s = m(s, h([0, e.charCodeAt(l + 14)], 48));
    case 14:
        s = m(s, h([0, e.charCodeAt(l + 13)], 40));
    case 13:
        s = m(s, h([0, e.charCodeAt(l + 12)], 32));
    case 12:
        s = m(s, h([0, e.charCodeAt(l + 11)], 24));
    case 11:
        s = m(s, h([0, e.charCodeAt(l + 10)], 16));
    case 10:
        s = m(s, h([0, e.charCodeAt(l + 9)], 8));
    case 9:
        s = m(s, [0, e.charCodeAt(l + 8)]),
        s = g(s, c),
        s = d(s, 33),
        s = g(s, u),
        i = m(i, s);
    case 8:
        a = m(a, h([0, e.charCodeAt(l + 7)], 56));
    case 7:
        a = m(a, h([0, e.charCodeAt(l + 6)], 48));
    case 6:
        a = m(a, h([0, e.charCodeAt(l + 5)], 40));
    case 5:
        a = m(a, h([0, e.charCodeAt(l + 4)], 32));
    case 4:
        a = m(a, h([0, e.charCodeAt(l + 3)], 24));
    case 3:
        a = m(a, h([0, e.charCodeAt(l + 2)], 16));
    case 2:
        a = m(a, h([0, e.charCodeAt(l + 1)], 8));
    case 1:
        a = m(a, [0, e.charCodeAt(l)]),
        a = g(a, u),
        a = d(a, 31),
        a = g(a, c),
        o = m(o, a)
    }
    return o = m(o, [0, e.length]),
    i = m(i, [0, e.length]),
    o = f(o, i),
    i = f(i, o),
    o = p(o),
    i = p(i),
    o = f(o, i),
    i = f(i, o),
    ("00000000" + (o[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (i[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (i[1] >>> 0).toString(16)).slice(-8)
}