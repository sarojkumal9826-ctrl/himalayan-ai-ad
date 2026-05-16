export default function HimalayanAd() { return ( <div className="min-h-screen bg-black text-white overflow-hidden"> {/* HERO SECTION */} <section className="relative h-screen flex items-center justify-center bg-cover bg-center" style={{ backgroundImage: "url('https://images.unsplash.com/photo-1516483638261-f4dbaf036963?q=80&w=1600&auto=format&fit=crop')", }} > <div className="absolute inset-0 bg-black/60"></div>

<div className="relative z-10 text-center px-6 max-w-4xl">
      <h1 className="text-5xl md:text-7xl font-bold leading-tight mb-6">
        Himalayan AI Mixologist
      </h1>

      <p className="text-xl md:text-2xl text-gray-300 mb-8">
        Inspired by Nepal. Powered by AI.
      </p>

      <button className="px-8 py-4 rounded-2xl bg-white text-black text-lg font-semibold hover:scale-105 transition-transform duration-300 shadow-2xl">
        Explore The Experience
      </button>
    </div>
  </section>

  {/* APP SHOWCASE */}
  <section className="py-24 px-6 bg-zinc-950">
    <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12 items-center">
      <div>
        <h2 className="text-4xl font-bold mb-6">
          AI Generated Cocktails
        </h2>

        <p className="text-gray-400 text-lg leading-relaxed mb-6">
          Generate luxury Himalayan-inspired cocktail recipes instantly
          using AI. Discover premium flavors, cinematic presentations,
          and creative drink ideas.
        </p>

        <div className="flex gap-4">
          <button className="px-6 py-3 rounded-xl bg-white text-black font-semibold">
            Open App
          </button>

          <button className="px-6 py-3 rounded-xl border border-white/20 hover:bg-white/10 transition">
            View Recipes
          </button>
        </div>
      </div>

      <div className="relative flex justify-center">
        <img
          src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=1000&auto=format&fit=crop"
          alt="Cocktail"
          className="rounded-3xl shadow-2xl w-full max-w-md object-cover"
        />
      </div>
    </div>
  </section>

  {/* BOOK SECTION */}
  <section className="py-24 px-6 bg-black">
    <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12 items-center">
      <div className="flex justify-center">
        <img
          src="https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=1000&auto=format&fit=crop"
          alt="Book"
          className="rounded-3xl shadow-2xl w-full max-w-sm"
        />
      </div>

      <div>
        <h2 className="text-4xl font-bold mb-6">
          The Himalayan Mixologist
        </h2>

        <p className="text-gray-400 text-lg leading-relaxed mb-8">
          A premium cocktail experience blending Himalayan inspiration,
          luxury mixology, and modern AI creativity.
        </p>

        <button className="px-8 py-4 rounded-2xl bg-white text-black font-semibold hover:scale-105 transition-transform duration-300">
          Discover The Book
        </button>
      </div>
    </div>
  </section>

  {/* COCKTAIL GALLERY */}
  <section className="py-24 px-6 bg-zinc-950">
    <div className="max-w-7xl mx-auto">
      <h2 className="text-5xl font-bold text-center mb-16">
        Signature Himalayan Cocktails
      </h2>

      <div className="grid md:grid-cols-3 gap-8">
        {[
          'https://images.unsplash.com/photo-1470337458703-46ad1756a187?q=80&w=1000&auto=format&fit=crop',
          'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?q=80&w=1000&auto=format&fit=crop',
          'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=1000&auto=format&fit=crop',
        ].map((image, index) => (
          <div
            key={index}
            className="group relative overflow-hidden rounded-3xl"
          >
            <img
              src={image}
              className="h-[500px] w-full object-cover group-hover:scale-110 transition-transform duration-700"
            />

            <div className="absolute inset-0 bg-gradient-to-t from-black/90 to-transparent"></div>

            <div className="absolute bottom-6 left-6">
              <h3 className="text-2xl font-bold mb-2">
                Himalayan Signature
              </h3>

              <p className="text-gray-300">
                Crafted with AI inspiration
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>

  {/* FINAL CTA */}
  <section className="relative py-32 px-6 text-center bg-cover bg-center"
    style={{
      backgroundImage:
        "url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1600&auto=format&fit=crop')",
    }}>
    <div className="absolute inset-0 bg-black/70"></div>

    <div className="relative z-10 max-w-4xl mx-auto">
      <h2 className="text-5xl md:text-7xl font-bold mb-8 leading-tight">
        Craft Cocktails With Himalayan AI
      </h2>

      <p className="text-xl text-gray-300 mb-10">
        Luxury mixology meets cinematic AI innovation.
      </p>

      <button className="px-10 py-5 rounded-2xl bg-white text-black text-xl font-bold hover:scale-105 transition-transform duration-300 shadow-2xl">
        Start The Experience
      </button>
    </div>
  </section>
</div>

); }
