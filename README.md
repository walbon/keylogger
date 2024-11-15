# Designing a Custom Keyboard Layout

This project is part of an experiment aimed at creating a customized keyboard layout suited for dual-language typing (pt_BR and en_US). The primary goal is to reduce the reliance on external keys and centralize typing to alleviate strain on weaker fingers, as I’ve been experiencing discomfort from my high weekly typing volume. By refining my layout, I hope to avoid RSI (Repetitive Strain Injury).

I explored alternative keyboard layouts, but they often cater to a single language rather than supporting both. Additionally, none seemed personalized enough to fit my needs, so I embarked on this project, starting with an incremental-output keylogger.

## The Daemon

The daemon, written primarily in Python, can start automatically or manually to detect and incrementally log keyboard events. Notably, I use Barrier, a virtual KVM switch, to manage seamless keyboard and mouse control across my dual workstations, where I conduct both work and research.

## Data Visualization

After capturing weekly typing data, I began visualizing keyboard usage patterns to inform layout redesign decisions. A bar graph, illustrating detected keystrokes, highlighted the high usage of multifunctional keys frequently accessed for tasks in tmux and neovim.

## Virtual Keyboard and Heat Map

Using Matplotlib, I created a virtual keyboard layout where color intensity indicates key usage frequency. This visual representation has already shown me that most usage tends to gravitate toward the outer edges of the keyboard—aside from the space bar, which sees constant use between words. This visualization has improved my understanding of which keys are frequently used.

<img src="https://walbon.github.io/images//usage-keyboard-full.png"/>

## Next Steps

My immediate next steps involve adjusting the layout of centrally positioned keys and reconfiguring shortcuts to use more accessible keys.

### Future Goals

Long-term goals include designing a split keyboard with custom keys, tailored specifically for dual-language use and to maximize typing comfort and efficiency.


