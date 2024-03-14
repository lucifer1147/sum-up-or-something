<script>
    import { goto } from '$app/navigation';

    const handleLogout = () => {
        localStorage.clear();
        goto('/');
    }
</script>

<div
	class="h-[100vh] w-full bg-gradient-to-r from-slate-700 to-slate-900 flex justify-center items-center flex-wrap"
>
	<div class="w-full flex justify-center flex-wrap">
		<h1 class="text-white text-4xl font-bold font-mono w-full h-12 text-center">
			Click the button below to logout
		</h1>
		<button on:click={handleLogout} class="bg-white w-1/2 h-12 rounded-3xl text-slate-800 font-mono text-3xl font-bold"
			>Logout</button
		>
	</div>
</div>
