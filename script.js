// IIFE Modules for Maa by Rigel

// --- Utility Functions ---
const fetchJSON = async (url) => {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    return await response.json();
  } catch (e) {
    console.error("Error fetching " + url, e);
    return null;
  }
};

// --- Language Module ---
const LangModule = (() => {
  let currentLang = localStorage.getItem('maa_lang') || 'en';
  let translations = {};

  const init = async () => {
    const mainSelector = document.getElementById('lang-selector');
    const welcomeSelector = document.getElementById('welcome-lang-selector');
    if (welcomeSelector && mainSelector) {
      welcomeSelector.innerHTML = mainSelector.innerHTML;
      welcomeSelector.value = currentLang;
    }

    if (!localStorage.getItem('maa_lang_selected')) {
      const modal = document.getElementById('welcome-lang-modal');
      if (modal) {
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';

        document.getElementById('welcome-lang-btn').addEventListener('click', () => {
          const selectedLang = welcomeSelector.value;
          setLanguage(selectedLang);
          mainSelector.value = selectedLang;
          localStorage.setItem('maa_lang_selected', 'true');
          modal.classList.add('hidden');
          document.body.style.overflow = '';
        });
      }
    }

    if (mainSelector) mainSelector.value = currentLang;
    if (mainSelector) {
      mainSelector.addEventListener('change', (e) => {
        setLanguage(e.target.value);
        localStorage.setItem('maa_lang_selected', 'true');
      });
    }
    await loadLanguage(currentLang);
  };

  const setLanguage = async (lang) => {
    currentLang = lang;
    localStorage.setItem('maa_lang', lang);
    await loadLanguage(lang);
    
    // Trigger Google Translate hidden dropdown
    const gtCombo = document.querySelector('.goog-te-combo');
    if (gtCombo) {
      gtCombo.value = lang;
      gtCombo.dispatchEvent(new Event('change'));
    }
  };

  const loadLanguage = async (lang) => {
    const data = await fetchJSON(`data/content_${lang}.json`);
    if (data) {
      translations = data;
      applyTranslations();
      // Also re-render dynamic content that relies on translations if needed
      ContentLoader.renderLearnCards(data.learn);
    }
  };

  const applyTranslations = () => {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const keys = key.split('.');
      let val = translations;
      keys.forEach(k => {
        if(val) val = val[k];
      });
      if (val) {
        el.textContent = val;
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      const keys = key.split('.');
      let val = translations;
      keys.forEach(k => {
        if(val) val = val[k];
      });
      if (val) {
        el.placeholder = val;
      }
    });
  };

  return { init, getTranslations: () => translations };
})();

// --- Content Loader Module ---
const ContentLoader = (() => {
  const init = async () => {
    const schemesData = await fetchJSON('data/schemes.json');
    if (schemesData && schemesData.schemes) {
      renderSchemeCards(schemesData.schemes);
    }

  };

  const renderLearnCards = (learnData) => {
    if(!learnData) return;
    const grid = document.getElementById('learn-grid');
    grid.innerHTML = `
      <div class="card learn-card">
        <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Basics" style="width: 100%; height: 160px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
        <h3>🩸 ${learnData.basics_title}</h3>
        <p>${learnData.basics_content}</p>
      </div>
      <div class="card learn-card">
        <img src="https://images.unsplash.com/photo-1584820927508-ea2b737d2870?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Hygiene" style="width: 100%; height: 160px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
        <h3>🧼 ${learnData.hygiene_title}</h3>
        <p>${learnData.hygiene_content}</p>
      </div>
      <div class="card learn-card">
        <img src="https://images.unsplash.com/photo-1532012197267-da84d127e765?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Myths" style="width: 100%; height: 160px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
        <h3>⚖️ ${learnData.myths_title}</h3>
        <p>${learnData.myths_content}</p>
      </div>
      <div class="card learn-card">
        <img src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Nutrition" style="width: 100%; height: 160px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
        <h3>🥗 ${learnData.nutrition_title}</h3>
        <p>${learnData.nutrition_content}</p>
      </div>
    `;
  };

  const renderSchemeCards = (schemes) => {
    const grid = document.getElementById('schemes-grid');
    grid.innerHTML = schemes.map(s => `
      <div class="scheme-card-rich" data-ministry="${s.tags[0]}">
        <div class="scheme-card-header">
          <span class="scheme-icon">${s.icon || '🏛️'}</span>
          <div class="scheme-card-header-text">
            <h3>${s.title}</h3>
            <span class="scheme-ministry-tag">${s.ministry}</span>
          </div>
        </div>
        <div class="scheme-card-body">
          <p>${s.description}</p>
          <ul class="scheme-benefits">
            ${s.benefits.map(b => `<li>✅ ${b}</li>`).join('')}
          </ul>
          <div class="scheme-eligibility">
            <strong>Eligibility:</strong> ${s.eligibility}
          </div>
        </div>
        <div class="scheme-card-footer">
          <span class="scheme-helpline-pill">📞 ${s.helpline}</span>
          <a href="${s.link}" target="_blank" rel="noopener" class="btn btn-primary btn-sm">Visit Portal ↗</a>
        </div>
      </div>
    `).join('');

    // Filter logic
    document.querySelectorAll('.scheme-filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.scheme-filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const ministry = btn.getAttribute('data-ministry');
        document.querySelectorAll('.scheme-card-rich').forEach(card => {
          const match = ministry === 'all' || card.getAttribute('data-ministry') === ministry;
          card.style.display = match ? 'flex' : 'none';
        });
      });
    });
  };



  return { init, renderLearnCards };
})();

// --- Tracker Module ---
const TrackerModule = (() => {
  const init = () => {
    const form = document.getElementById('tracker-form');
    const resetBtn = document.getElementById('reset-tracker');
    
    loadFromStorage();
    setupSymptomLogger();

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const lastPeriod = document.getElementById('last-period').value;
      const cycleLength = parseInt(document.getElementById('cycle-length').value, 10);
      calculateAndSave(lastPeriod, cycleLength);
    });

    resetBtn.addEventListener('click', () => {
      localStorage.removeItem('maa_tracker');
      localStorage.removeItem('maa_symptoms');
      document.getElementById('tracker-result').classList.add('hidden');
      form.reset();
      
      document.querySelectorAll('.tag-btn').forEach(btn => btn.classList.remove('active'));
    });
  };

  const setupSymptomLogger = () => {
    const todayStr = new Date().toISOString().split('T')[0];
    let symptomsLog = JSON.parse(localStorage.getItem('maa_symptoms') || '{}');
    const todaySymptoms = symptomsLog[todayStr] || [];

    const buttons = document.querySelectorAll('.tag-btn');
    const msg = document.getElementById('log-msg');

    buttons.forEach(btn => {
      if (todaySymptoms.includes(btn.dataset.symptom)) {
        btn.classList.add('active');
      }

      btn.addEventListener('click', () => {
        const symptom = btn.dataset.symptom;
        if (btn.classList.contains('active')) {
          btn.classList.remove('active');
          const index = todaySymptoms.indexOf(symptom);
          if (index > -1) todaySymptoms.splice(index, 1);
          msg.textContent = "Symptom removed.";
        } else {
          btn.classList.add('active');
          todaySymptoms.push(symptom);
          msg.textContent = "Logged for today! Tracking helps identify patterns.";
        }
        
        symptomsLog[todayStr] = todaySymptoms;
        localStorage.setItem('maa_symptoms', JSON.stringify(symptomsLog));
        
        setTimeout(() => { msg.textContent = ""; }, 3000);
      });
    });
  };

  const calculateAndSave = (lastPeriodStr, cycleLength) => {
    const lastDate = new Date(lastPeriodStr);
    
    // Next period
    const nextDate = new Date(lastDate);
    nextDate.setDate(lastDate.getDate() + cycleLength);
    
    // Fertile window (approx 14 days before next period, 5 days window)
    const ovulationDate = new Date(nextDate);
    ovulationDate.setDate(nextDate.getDate() - 14);
    
    const fertileStart = new Date(ovulationDate);
    fertileStart.setDate(ovulationDate.getDate() - 2);
    
    const fertileEnd = new Date(ovulationDate);
    fertileEnd.setDate(ovulationDate.getDate() + 2);

    const data = {
      lastPeriod: lastPeriodStr,
      cycleLength,
      nextDate: nextDate.toISOString(),
      fertileStart: fertileStart.toISOString(),
      fertileEnd: fertileEnd.toISOString()
    };
    
    localStorage.setItem('maa_tracker', JSON.stringify(data));
    displayResult(data);
  };

  const displayResult = (data) => {
    const lastDate = new Date(data.lastPeriod);
    const nextDateObj = new Date(data.nextDate);
    document.getElementById('next-date').textContent = nextDateObj.toDateString();
    
    const fStart = new Date(data.fertileStart);
    const fEnd = new Date(data.fertileEnd);
    document.getElementById('fertile-dates').textContent = `${fStart.toDateString()} - ${fEnd.toDateString()}`;
    
    // Calculate current cycle day
    const today = new Date();
    today.setHours(0,0,0,0);
    lastDate.setHours(0,0,0,0);
    nextDateObj.setHours(0,0,0,0);
    
    const diffTimeSinceLast = today - lastDate;
    let cycleDay = Math.floor(diffTimeSinceLast / (1000 * 60 * 60 * 24)) + 1;
    
    // If we've passed the next expected period and user hasn't logged it
    if (cycleDay > data.cycleLength || cycleDay <= 0) {
      cycleDay = "Unknown (Please log your new period)";
      document.getElementById('current-cycle-day').textContent = cycleDay;
      document.getElementById('current-phase-name').textContent = "Pending Log";
      document.getElementById('current-phase-insight').textContent = "Did your period start? Please log your new start date to continue tracking.";
      document.getElementById('cycle-progress-fill').style.width = '0%';
    } else {
      document.getElementById('current-cycle-day').textContent = cycleDay;
      
      // Determine phase
      let phaseName = "";
      let phaseInsight = "";
      let phaseColor = "";
      
      const ovulationDay = data.cycleLength - 14;
      
      if (cycleDay <= 5) {
        phaseName = "Menstrual Phase";
        phaseInsight = "Your body is shedding the uterine lining. Rest if needed, and eat iron-rich foods like spinach and lentils.";
        phaseColor = "var(--color-crimson)";
      } else if (cycleDay < ovulationDay - 2) {
        phaseName = "Follicular Phase";
        phaseInsight = "Estrogen is rising! You might feel a boost in energy and creativity. Great time for exercise and planning.";
        phaseColor = "var(--color-primary)";
      } else if (cycleDay >= ovulationDay - 2 && cycleDay <= ovulationDay + 2) {
        phaseName = "Ovulation Phase";
        phaseInsight = "An egg is being released. You are in your fertile window. Estrogen and testosterone peak now.";
        phaseColor = "var(--color-peach)";
      } else {
        phaseName = "Luteal Phase";
        phaseInsight = "Progesterone is high, which might make you feel calmer but can also trigger PMS. Gentle yoga and hydration help.";
        phaseColor = "var(--color-sand)";
      }
      
      document.getElementById('current-phase-name').textContent = phaseName;
      document.getElementById('current-phase-insight').textContent = phaseInsight;
      
      // Progress bar
      const progressPercent = (cycleDay / data.cycleLength) * 100;
      const progressFill = document.getElementById('cycle-progress-fill');
      progressFill.style.width = `${progressPercent}%`;
      progressFill.style.background = phaseColor;
    }
    
    // Calculate countdown
    const diffTime = nextDateObj - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    document.getElementById('days-countdown').textContent = diffDays >= 0 ? diffDays : 0;
    document.getElementById('tracker-result').classList.remove('hidden');
  };

  const loadFromStorage = () => {
    const saved = localStorage.getItem('maa_tracker');
    if (saved) {
      const data = JSON.parse(saved);
      document.getElementById('last-period').value = data.lastPeriod;
      document.getElementById('cycle-length').value = data.cycleLength;
      displayResult(data);
    }
  };

  return { init };
})();

// --- Q&A Module ---
const QAModule = (() => {
  let knowledgeBase = [];
  let qnaBase = [];

  const DEMO_ANSWERS = {
    "General": "Every body is different. Cycle lengths and symptoms can vary slightly from month to month. Tracking helps identify your unique pattern.",
    "Hygiene": "It's important to change your pad or tampon every 4-6 hours to prevent infection. Wash your hands before and after.",
    "Health": "If you experience severe pain that prevents daily activities, consult a healthcare professional. Tracking your basal body temperature and resting heart rate can also provide insights into hormonal health.",
    "Nutrition": "Eating iron-rich foods and staying hydrated mitigates cramps. Research shows metabolic shifts during different cycle phases can affect glucose levels, so a balanced diet is crucial.",
    "Emotional": "Hormonal shifts are natural. Research comparing menstrual cycles to daily/seasonal rhythms shows profound impacts on mood. Practice self-care, and adjust your routine according to your energy levels.",
    "Urbanization": "Urban environments can increase access to products but also introduce stress and dietary changes that may cause cycle irregularities. Maintaining a healthy lifestyle is key."
  };

  const init = async () => {
    try {
      const res = await fetch('data/conditions.json');
      knowledgeBase = await res.json();
      const resQna = await fetch('data/qna.json');
      qnaBase = await resQna.json();
    } catch (e) {
      console.error("Failed to load medical knowledge base", e);
    }

    const form = document.getElementById('qa-form');
    loadQuestions();

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const text = document.getElementById('qa-input').value;
      const category = document.getElementById('qa-category').value;
      
      const answer = generateAnswer(text, category);
      
      const newQ = {
        id: Date.now(),
        text,
        category,
        timestamp: new Date().toISOString(),
        answer: answer
      };
      
      const questions = getQuestions();
      questions.unshift(newQ);
      localStorage.setItem('maa_qa', JSON.stringify(questions));
      
      form.reset();
      loadQuestions();
    });

    const clearBtn = document.getElementById('qa-clear-btn');
    if (clearBtn) {
      clearBtn.addEventListener('click', (e) => {
        e.preventDefault();
        localStorage.removeItem('maa_qa');
        const formEl = document.getElementById('qa-form');
        if (formEl) formEl.reset();
        loadQuestions();
        alert('Your Q&A data has been successfully cleared.');
      });
    }
  };

  const SYNONYMS = {
    "pcod": ["pcos", "ovarian cyst"],
    "pain": ["cramps", "ache", "hurts", "sore", "dysmenorrhea"],
    "period": ["menstruation", "cycle", "flow", "bleeding"],
    "late": ["delayed", "missed", "no period", "skip"],
    "heavy": ["excessive", "clots", "too much"],
    "mood": ["angry", "sad", "crying", "emotional", "depressed", "anxious", "mood swings"],
    "tired": ["fatigue", "exhausted", "low energy", "sleepy", "weak"],
    "spotting": ["brown discharge", "light bleeding", "pink discharge"],
    "acne": ["pimples", "breakouts", "zits"]
  };

  const normalizeText = (text) => {
    let normalized = text.toLowerCase().replace(/[^\w\s]/g, ' ');
    Object.keys(SYNONYMS).forEach(key => {
      SYNONYMS[key].forEach(syn => {
        if (normalized.includes(syn)) {
          normalized += ` ${key}`; // Append core keyword to boost score
        }
      });
    });
    return normalized;
  };

  const generateAnswer = (question, category) => {
    if ((!knowledgeBase || knowledgeBase.length === 0) && (!qnaBase || qnaBase.length === 0)) {
      return DEMO_ANSWERS[category] || "Thank you for asking. Our experts are reviewing this.";
    }

    const qLower = normalizeText(question);
    const words = qLower.split(/\s+/).filter(w => w.length > 2);
    
    // Score QnA base
    const scoredQnA = qnaBase.map(item => {
      let score = 0;
      const itemQ = (item.question || "").toLowerCase();
      const keywords = Array.isArray(item.keywords) ? item.keywords.map(k => k.toLowerCase()) : [];
      
      keywords.forEach(kw => {
        if (qLower.includes(kw)) score += 5;
      });
      
      words.forEach(w => {
        if (itemQ.includes(w)) score += 2;
      });
      
      return { type: 'qna', item, score };
    }).filter(c => c.score > 2);

    // Score Conditions
    const scoredConditions = knowledgeBase.map(item => {
      let score = 0;
      
      const conditionName = (item.condition || "").toLowerCase();
      const keywords = Array.isArray(item.keywords) ? item.keywords.map(k => k.toLowerCase()) : [];
      const symptoms = (item.symptoms || "").toLowerCase();
      
      if (conditionName && qLower.includes(conditionName)) score += 10;
      
      keywords.forEach(kw => {
        if (qLower.includes(kw)) score += 5;
      });
      
      words.forEach(w => {
        if (symptoms.includes(w)) score += 1;
      });
      
      return { type: 'condition', item, score };
    }).filter(c => c.score > 1);

    const allMatches = [...scoredQnA, ...scoredConditions];
    allMatches.sort((a, b) => b.score - a.score);

    if (allMatches.length > 0) {
      const topMatches = allMatches.slice(0, 2);
      
      let response = `Based on your question, we found ${topMatches.length > 1 ? 'these possible answers' : 'this possible answer'}:\n<br><br>\n`;
      
      let highRisk = false;
      let doctorRequired = false;

      topMatches.forEach((match, index) => {
        if (match.type === 'qna') {
          response += `<strong>${index + 1}. Q: ${match.item.question}</strong>\n<br>\n`;
          response += `<strong>A:</strong> ${match.item.answer.replace(/\n/g, '<br>')}\n<br><br>\n`;
        } else {
          const bestMatch = match.item;
          if (bestMatch.doctor_required || bestMatch.risk_level === 'high') {
            highRisk = true;
            doctorRequired = true;
          }
          
          response += `<strong>${index + 1}. ${bestMatch.condition}</strong> (${bestMatch.description || 'Condition'})\n<br>\n`;
          if (bestMatch.symptoms) response += `- <strong>Symptoms:</strong> ${bestMatch.symptoms}\n<br>\n`;
          if (bestMatch.causes) response += `- <strong>Causes:</strong> ${bestMatch.causes}\n<br>\n`;
          if (bestMatch.recommendation) response += `- <strong>Recommendation:</strong> ${bestMatch.recommendation}\n<br><br>\n`;
        }
      });

      if (doctorRequired || highRisk) {
        response += `⚠️ <em>This website is only for general suggestion. Please consult your nearest gynecologist or healthcare professional for an accurate diagnosis.</em>`;
      } else {
        response += `💡 <em>This website is only for general suggestion. Please consult your nearest gynecologist. Tracking your symptoms daily can also help you understand your cycle better.</em>`;
      }
      return response.trim();
    }
    
    // Fallback if no strong match
    return DEMO_ANSWERS[category] || "Thank you for sharing. This website is only for general suggestion. Please consult your nearest gynecologist.";
  };

  const getQuestions = () => {
    const data = localStorage.getItem('maa_qa');
    return data ? JSON.parse(data) : [];
  };

  const loadQuestions = () => {
    const questions = getQuestions();
    const list = document.getElementById('qa-list');
    
    if (questions.length === 0) {
      list.innerHTML = `<p style="text-align:center; color:var(--color-text-muted);">No questions yet. Be the first to ask!</p>`;
      return;
    }
    
    list.innerHTML = questions.map(q => `
      <div class="qa-card">
        <div class="qa-meta">
          <span class="badge">${q.category}</span>
          <span>${new Date(q.timestamp).toLocaleDateString()}</span>
        </div>
        <p class="qa-question">Q: ${q.text}</p>
        <p class="qa-answer">A: ${q.answer}</p>
      </div>
    `).join('');
  };

  return { init };
})();

// --- Animation & UI Module ---
const UIModule = (() => {
  const init = () => {
    // Mobile Menu Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    
    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', !isExpanded);
      mobileMenu.classList.toggle('hidden');
    });

    document.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.classList.add('hidden');
      });
    });

    // Scroll Animations (Intersection Observer)
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          
          // Counters
          if(entry.target.id === 'impact') {
            startCounters();
            observer.unobserve(entry.target); // only once
          }
        }
      });
    }, { threshold: 0.15 });

    document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
  };

  const startCounters = () => {
    document.querySelectorAll('.counter').forEach(counter => {
      const target = +counter.getAttribute('data-target');
      const duration = 2000;
      const stepTime = Math.abs(Math.floor(duration / target));
      let current = 0;
      const increment = target / (duration / 30); // 30ms intervals
      
      const timer = setInterval(() => {
        current += increment;
        if(current >= target) {
          counter.textContent = target.toLocaleString() + (counter.hasAttribute('data-no-plus') ? '' : '+');
          clearInterval(timer);
        } else {
          counter.textContent = Math.floor(current).toLocaleString();
        }
      }, 30);
    });
  };

  return { init };
})();

// --- Blogs Module ---
const BlogsModule = (() => {
  const init = async () => {
    try {
      const res = await fetch('data/blog.json');
      const blogs = await res.json();
      renderBlogs(blogs);
    } catch (e) {
      console.error("Failed to load blogs", e);
    }

    const closeBtn = document.getElementById('close-blog-modal');
    const modal = document.getElementById('blog-modal');
    if (closeBtn && modal) {
      closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
      modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.add('hidden');
      });
    }
  };

  const renderBlogs = (blogs) => {
    const grid = document.getElementById('blog-grid');
    if (!grid) return;
    grid.innerHTML = blogs.map(blog => `
      <a href="blog.html#${blog.id}" class="card blog-card" style="text-align: left; text-decoration: none; display: block;">
        <img src="${blog.image}" alt="${blog.title}" style="width: 100%; height: 200px; object-fit: cover; border-radius: var(--radius-lg); margin-bottom: 1rem;">
        <h3 style="color: var(--color-crimson); margin-bottom: 0.5rem; font-family: var(--font-display);">${blog.title}</h3>
        <p style="color: var(--color-text-muted); font-size: 0.95rem; margin-bottom: 1rem;">${blog.excerpt}</p>
        <span style="font-weight: 600; color: var(--color-crimson); font-size: 0.9rem;">Read More →</span>
      </a>
    `).join('');

    window.siteBlogs = blogs;
  };

  return { init };
})();

// --- PDF Insights Tabs Module ---
const TabsModule = (() => {
  const init = () => {
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-tab');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        const panel = document.getElementById('tab-' + target);
        if (panel) panel.classList.add('active');
      });
    });
  };
  return { init };
})();

// --- App Bootstrap ---
document.addEventListener('DOMContentLoaded', () => {
  LangModule.init();
  ContentLoader.init();
  TrackerModule.init();
  QAModule.init();
  UIModule.init();
  TabsModule.init();
  BlogsModule.init();
  
  // SOS Modal Logic
  const sosBtn = document.getElementById('sos-btn');
  const sosModal = document.getElementById('sos-modal');
  const closeSosBtn = document.getElementById('close-sos-modal');
  if (sosBtn && sosModal) {
    sosBtn.addEventListener('click', () => {
      sosModal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    });
    closeSosBtn.addEventListener('click', () => {
      sosModal.classList.add('hidden');
      document.body.style.overflow = '';
    });
    sosModal.addEventListener('click', (e) => {
      if (e.target === sosModal) {
        sosModal.classList.add('hidden');
        document.body.style.overflow = '';
      }
    });
  }
});
