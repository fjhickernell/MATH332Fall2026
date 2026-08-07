<script>
  // Shared semantic notation for MathJax in Quarto RevealJS slides.
  // A string defines a zero-argument macro; [replacement, n] defines one
  // with n arguments. Backslashes are escaped for JavaScript strings.
  // The companion hickernell-latex-macros.tex is not yet synchronized with
  // this registry; equivalent definitions should eventually share one source.
  window.MathJax = {
    startup: {
      typeset: false,
      pageReady: () => {
        const typesetAndLayout = (() => {
          let busy = false;
          let queued = false;

          const run = async () => {
            if (busy) {
              queued = true;
              return;
            }
            busy = true;
            queued = false;

            try {
              await MathJax.typesetPromise();
              if (window.Reveal && typeof Reveal.layout === "function") {
                Reveal.layout();
              }
            } finally {
              busy = false;
              if (queued) {
                requestAnimationFrame(run);
              }
            }
          };

          return () => requestAnimationFrame(run);
        })();

        return MathJax.startup.defaultPageReady().then(() => {
          if (window.Reveal) {
            Reveal.on("ready", typesetAndLayout);
            Reveal.on("slidechanged", typesetAndLayout);
            Reveal.on("fragmentshown", typesetAndLayout);
            Reveal.on("fragmenthidden", typesetAndLayout);
          }
          typesetAndLayout();
        });
      }
    },
    
    svg: {
      mtextInheritFont: true,
      fontCache: "global"
    },
    
    tex: {
      macros: {

        // Presentation helpers
        mathlink: ["\\href{#1}{\\text{\\color{##0f8b8d}{#2}}}", 2],
        yamlref: ["{\\text{#1}}", 1],
        frag: ["{\\class{fragment}{#2}}", 2],
        alert: ["{\\class{alert}{#1}}", 1],
        alerttext: ["{\\class{alert}{\\text{#1}}}", 1],
        alerttextsf: ["{\\class{alert}{\\textsf{#1}}}",1],
        mat: ["{\\mathsf{#1}}", 1],
        vct: ["{\\boldsymbol{#1}}", 1],
        notimplies: "\\ \\mathrel{\\not\\!\\!\\!\\Longrightarrow}",
        convas: ["\\xrightarrow{\\mathsf{a.s.}}", 0],
        convp:  ["\\xrightarrow{\\Prob}", 0],
        convd:  ["\\xrightarrow{\\mathsf{d}}", 0],

        nconvas: ["\\mathrel{\\;\\not\\!\\!\\!\\xrightarrow{\\mathsf{a.s.}}}", 0],
        nconvp:  ["\\mathrel{\\;\\not\\!\\xrightarrow{\\Prob}}", 0],
        nconvd:  ["\\mathrel{\\;\\not\\!\\xrightarrow{\\mathsf{d}}}", 0],

        asto: ["\\xrightarrow{\\mathsf{a.s.}}", 0],
        pto:  ["\\xrightarrow{\\Prob}", 0],
        dto:  ["\\xrightarrow{\\mathsf{d}}", 0],

        // Common mathematical operators
        success: "{\\operatorname{succ}}",
        sinc:    "{\\operatorname{sinc}}",
        sech:    "{\\operatorname{sech}}",
        csch:    "{\\operatorname{csch}}",

        // Probability and expectation; exercise notation uses exstar below
        Prob: "{\\mathbb{P}}",
        Ex:   "{\\mathbb{E}}", // expectation, not exercise


        dist:  "{\\operatorname{dist}}",
        Dsc:  "{\\operatorname{D}}",
        ESD:  "{\\operatorname{ESD}}",
        WESD:  "{\\operatorname{WESD}}",
        Vtn:   "{\\operatorname{V}}",
        spn:   "{\\operatorname{span}}",
        sgn:   "{\\operatorname{sgn}}",
        releff: "{\\operatorname{rel-eff}}",
        mse:   "{\\operatorname{mse}}",
        rmse:  "{\\operatorname{rmse}}",
        rank:  "{\\operatorname{rank}}",
        erfc:  "{\\operatorname{erfc}}",
        erf:   "{\\operatorname{erf}}",
        cov:   "{\\operatorname{cov}}",
        cost:  "{\\operatorname{cost}}",
        comp:  "{\\operatorname{comp}}",
        corr:  "{\\operatorname{corr}}",
        diag:  "{\\operatorname{diag}}",
        power: "{\\operatorname{power}}",
        var:   "{\\operatorname{var}}",
        opt:   "{\\operatorname{opt}}",
        brandnew: "{\\operatorname{new}}",
        std:   "{\\operatorname{std}}",
        se:    "{\\operatorname{se}}",
        kurt:  "{\\operatorname{kurt}}",
        med:   "{\\operatorname{med}}",
        vol:   "{\\operatorname{vol}}",
        bias:  "{\\operatorname{bias}}",
        RR:   "{\\mathcal{R}}",
        SS:   "{\\operatorname{SS}}",
        RSS:  "{\\operatorname{RSS}}",
        SST:  "{\\operatorname{SST}}",
        SSR:  "{\\operatorname{SSR}}",
        SSB:  "{\\operatorname{SSB}}",
        SSW:  "{\\operatorname{SSW}}",
        MSB:  "{\\operatorname{MSB}}",
        MSW:  "{\\operatorname{MSW}}",

        // Probability distributions
        Bern:  "{\\operatorname{Bern}}",
        Bin:   "{\\operatorname{Bin}}",
        Unif:  "{\\operatorname{Unif}}",
        Norm:  "{\\operatorname{Norm}}",
        Exp:   "{\\operatorname{Exp}}",
        Gam:   "{\\operatorname{Gamma}}",
        Pois:  "{\\operatorname{Pois}}",
        Geom:  "{\\operatorname{Geom}}",
        Cauchy:"{\\operatorname{Cauchy}}",
        Laplace:"{\\operatorname{Laplace}}",
        Beta:  "{\\operatorname{Beta}}",
        Weibull:"{\\operatorname{Weibull}}",
        Lognorm:"{\\operatorname{Lognormal}}",
        GP:     "{\\operatorname{GP}}",

        argmin: ["\\operatorname*{argmin}", 0],
        argmax: ["\\operatorname*{argmax}", 0],
        Argmin: ["\\argmin\\limits_{#1}", 1],
        Argmax: ["\\argmax\\limits_{#1}", 1],

        sign:  "{\\operatorname{sign}}",
        spann: "{\\operatorname{span}}",
        cond:  "{\\operatorname{cond}}",
        trace: "{\\operatorname{trace}}",
        det:   "{\\operatorname{det}}",
        Si:    "{\\operatorname{Si}}",
        col:   "{\\operatorname{col}}",
        nullspace: "{\\operatorname{null}}",
        Order: "{\\mathcal{O}}",
        logit: "{\\operatorname{logit}}",
        probit: "{\\operatorname{probit}}",

        IIDsim: "\\mathrel{\\stackrel{\\mathrm{IID}}{\\sim}}",
        LDsim:  "\\mathrel{\\stackrel{\\mathrm{LD}}{\\sim}}",
        appxsim: "\\mathrel{\\stackrel{\\cdot}{\\sim}}",

        naturals:  "{\\mathbb{N}}",
        natzero:   "{\\mathbb{N}_0}",
        integers:  "{\\mathbb{Z}}",
        rationals: "{\\mathbb{Q}}",
        reals:     "{\\mathbb{R}}",
        complex:   "{\\mathbb{C}}",
        bbone:     "{\\mathbb{1}}",
        indic:     "{\\mathop{\\mathchoice{\\large\\mathbb{1}}{\\large\\mathbb{1}}{\\mathbb{1}}{\\mathbb{1}}}}",  // indic: enlarged blackboard-bold indicator (uses mathchoice so subscripts scale)

        abs:  ["{\\left\\lvert #1 \\right\\rvert}", 1],
        norm: ["{\\left\\lVert #1 \\right\\rVert}", 1],
        ip:   ["{\\left\\langle #1, #2 \\right\\rangle}", 2],
        dim:   "{\\operatorname{dim}}",
        df:   "{\\mathrm{df}}",
        SE:   "{\\operatorname{SE}}",


        bvec: ["{\\boldsymbol{#1}}", 1],
        avec: ["{\\vec{#1}}", 1],
        vecsym: ["{\\boldsymbol{#1}}", 1],

        va:  "{\\boldsymbol{a}}",
        vb:  "{\\boldsymbol{b}}",
        vc:  "{\\boldsymbol{c}}",
        vd:  "{\\boldsymbol{d}}",
        ve:  "{\\boldsymbol{e}}",
        vf:  "{\\boldsymbol{f}}",
        vg:  "{\\boldsymbol{g}}",
        vh:  "{\\boldsymbol{h}}",
        vi:  "{\\boldsymbol{i}}",
        vj:  "{\\boldsymbol{j}}",
        vk:  "{\\boldsymbol{k}}",
        vl:  "{\\boldsymbol{l}}",
        vm:  "{\\boldsymbol{m}}",
        vn:  "{\\boldsymbol{n}}",
        vo:  "{\\boldsymbol{o}}",
        vp:  "{\\boldsymbol{p}}",
        vq:  "{\\boldsymbol{q}}",
        vr:  "{\\boldsymbol{r}}",
        vs:  "{\\boldsymbol{s}}",
        vt:  "{\\boldsymbol{t}}",
        vu:  "{\\boldsymbol{u}}",
        vv:  "{\\boldsymbol{v}}",
        vw:  "{\\boldsymbol{w}}",
        vx:  "{\\boldsymbol{x}}",
        vy:  "{\\boldsymbol{y}}",
        vz:  "{\\boldsymbol{z}}",

        vA:  "{\\boldsymbol{A}}",
        vB:  "{\\boldsymbol{B}}",
        vC:  "{\\boldsymbol{C}}",
        vD:  "{\\boldsymbol{D}}",
        vE:  "{\\boldsymbol{E}}",
        vF:  "{\\boldsymbol{F}}",
        vG:  "{\\boldsymbol{G}}",
        vH:  "{\\boldsymbol{H}}",
        vI:  "{\\boldsymbol{I}}",
        vJ:  "{\\boldsymbol{J}}",
        vK:  "{\\boldsymbol{K}}",
        vL:  "{\\boldsymbol{L}}",
        vM:  "{\\boldsymbol{M}}",
        vN:  "{\\boldsymbol{N}}",
        vO:  "{\\boldsymbol{O}}",
        vP:  "{\\boldsymbol{P}}",
        vQ:  "{\\boldsymbol{Q}}",
        vR:  "{\\boldsymbol{R}}",
        vS:  "{\\boldsymbol{S}}",
        vT:  "{\\boldsymbol{T}}",
        vU:  "{\\boldsymbol{U}}",
        vV:  "{\\boldsymbol{V}}",
        vW:  "{\\boldsymbol{W}}",
        vX:  "{\\boldsymbol{X}}",
        vY:  "{\\boldsymbol{Y}}",
        vZ:  "{\\boldsymbol{Z}}",

        
        tvf: "{\\widetilde{\\boldsymbol{f}}}",
        tvy: "{\\widetilde{\\boldsymbol{y}}}",
        
        tg:  "{\\widetilde{g}}",
        tK:  "{\\widetilde{K}}",
        tX:  "{\\widetilde{X}}",
        tY:  "{\\widetilde{Y}}",
        tZ:  "{\\widetilde{Z}}",
        tildeh: "{\\widetilde{h}}",

        valpha: "{\\boldsymbol{\\alpha}}",
        vbeta:  "{\\boldsymbol{\\beta}}",
        vgamma: "{\\boldsymbol{\\gamma}}",
        vdelta: "{\\boldsymbol{\\delta}}",
        vDelta: "{\\boldsymbol{\\Delta}}",
        vepsilon: "{\\boldsymbol{\\epsilon}}",
        vveps: "{\\boldsymbol{\\varepsilon}}",
        vlambda:  "{\\boldsymbol{\\lambda}}",
        vsigma:   "{\\boldsymbol{\\sigma}}",
        vtheta:   "{\\boldsymbol{\\theta}}",
        vTheta:   "{\\boldsymbol{\\Theta}}",
        vomega:   "{\\boldsymbol{\\omega}}",
        vpi:      "{\\boldsymbol{\\pi}}",
        vphi:     "{\\boldsymbol{\\phi}}",
        vPhi:     "{\\boldsymbol{\\Phi}}",
        vmu:      "{\\boldsymbol{\\mu}}",
        vnu:     "{\\boldsymbol{\\nu}}",
        vzeta:   "{\\boldsymbol{\\zeta}}",

        mA: "{\\mathsf{A}}",
        mH: "{\\mathsf{H}}",
        mX: "{\\mathsf{X}}",
        mW: "{\\mathsf{W}}",
        mP: "{\\mathsf{P}}",
        mQ: "{\\mathsf{Q}}",
        mR: "{\\mathsf{R}}",
        mI: "{\\mathsf{I}}",
        mzero: "{\\mathsf{0}}",
        mone: "{\\mathsf{1}}",

        htheta: "{\\widehat{\\theta}}",
        hvtheta: "{\\widehat{\\boldsymbol{\\theta}}}",
        tvtheta: "{\\widetilde{\\boldsymbol{\\theta}}}",
        hTheta: "{\\widehat{\\Theta}}",
        hbeta:  "{\\widehat{\\beta}}",
        hvbeta: "{\\widehat{\\boldsymbol{\\beta}}}",
        hlambda: "{\\widehat{\\lambda}}",
        hmu:    "{\\widehat{\\mu}}",
        hvmu:   "{\\widehat{\\boldsymbol{\\mu}}}",
        hsigma: "{\\widehat{\\sigma}}",
        hSigma: "{\\widehat{\\Sigma}}",
        hp:    "{\\widehat{p}}",
        hJ:    "{\\widehat{J}}",
        hf:    "{\\widehat{f}}",
        hF:    "{\\widehat{F}}",
        hP:     "{\\widehat{P}}",
        hX:     "{\\widehat{X}}",
        hY:     "{\\widehat{Y}}",
        hvY:    "{\\widehat{\\boldsymbol{Y}}}",
        hZ:     "{\\widehat{Z}}",
        hveps:   "{\\widehat{\\varepsilon}}",
        hvveps: "{\\widehat{\\boldsymbol{\\varepsilon}}}",

        ct: "{\\mathcal{T}}",
        ch: "{\\mathcal{H}}",
        ck: "{\\mathcal{K}}",
        cf: "{\\mathcal{F}}",
        cc: "{\\mathcal{C}}",
        cx: "{\\mathcal{X}}",

        vzero: "{\\boldsymbol{0}}",
        vone:  "{\\boldsymbol{1}}",
        vinf:  "{\\boldsymbol{\\infty}}",
        
        barD: "{\\overline{D}}",
        barx: "{\\overline{x}}",
        barX: "{\\overline{X}}",
        barY: "{\\overline{Y}}",
        bary: "{\\overline{y}}",
        barZ: "{\\overline{Z}}",

        me:  "{\\mathrm{e}}",
        mi:  "{\\mathrm{i}}",
        mpi: "{\\mathrm{\\pi}}",
        mK: "{\\mathsf{K}}",
        tmK: "{\\widetilde{\\mathsf{K}}}",
        mSigma: "{\\mathsf{\\Sigma}}",

        dif: "{\\mathrm{d}}",
        IID: "{\\mathrm{IID}}",
        MLE: "{\\mathrm{MLE}}",
        LRT: "{\\mathrm{LRT}}",

        // Exercise markers and exercise-specific relations
        exstar: "{\\mathop{\\mathchoice{\\color{gold}{\\Large\\star}}{\\color{gold}{\\Large\\star}}{\\color{gold}{\\large\\star}}{\\color{gold}{\\star}}}}",
        exeq: "{\\mathrel{\\,\\overset{\\exstar}{=}\\,}}",
        exsim: "{\\mathrel{\\,\\overset{\\exstar}{\\sim}\\,}}",
        
      } 
    }
  };
</script>
